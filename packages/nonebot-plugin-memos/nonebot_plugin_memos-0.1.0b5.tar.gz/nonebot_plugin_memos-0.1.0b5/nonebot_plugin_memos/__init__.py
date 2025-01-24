from json import loads
from typing import Any
from nonebot import require

require("nonebot_plugin_alconna")
require("nonebot_plugin_orm")
require("nonebot_plugin_session")
require("nonebot_plugin_session_orm")

from nonebot.plugin import PluginMetadata
from nonebot.plugin import inherit_supported_adapters
from sqlalchemy import select

from .cache import get_client
from .config import Config
from .db import Memo, Setting
from .client import ApiClient


from nonebot_plugin_session_orm import get_session_persist_id
from nonebot_plugin_alconna import Match, UniMessage, on_alconna
from arclet.alconna import Alconna, Arg, Args, Subcommand
from nonebot_plugin_session import EventSession
from nonebot_plugin_orm import async_scoped_session

__plugin_metadata__ = PluginMetadata(
    name="memos",
    description="plugin for memos",
    usage="memos help",
    type="application",
    homepage="https://github.com/eya46/nonebot_plugin_memos",
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna", "nonebot_plugin_session"),
    config=Config,
)


memos = on_alconna(
    Alconna(
        "memos",
        Subcommand("bind", Args["url", str]["token", str]),
        Subcommand("list"),
        Subcommand("default", Arg("memo_id", int)),
        Subcommand("delete", Arg("memo_id", int)),
        Subcommand("create", Arg("content", str, seps="\n")),
    )
)


@memos.assign("bind")
async def bind_handler(
    url: Match[str],
    token: Match[str],
    session: EventSession,
    sqlSession: async_scoped_session,
):
    if session.level != 1:
        return await UniMessage("请在私聊中使用此命令").send()

    user_info = "null"

    try:
        client = ApiClient(url.result, token.result)
        resp = await client.getAuthStatus()
        if resp.status_code != 200:
            return await UniMessage("memos身份校验失败!").send()
        user_info = resp.text
    except Exception as e:
        return await UniMessage(f"检查memos服务失败: {e}").send()

    session_persist_id = await get_session_persist_id(session)

    memo = await sqlSession.scalar(
        select(Memo).where(Memo.user_id == session.id1).where(Memo.session_persist_id == session_persist_id)
    )

    setting = await sqlSession.scalar(select(Setting).where(Setting.user_id == session.id1))

    if memo:
        memo.url = url.result
        memo.token = token.result
        memo.user_info = user_info
        sqlSession.add(memo)
        await UniMessage("更新绑定成功!").send()
    else:
        memo = Memo(
            user_id=session.id1,
            user_info=user_info,
            session_persist_id=session_persist_id,
            url=url.result,
            token=token.result,
        )
        sqlSession.add(memo)
        await sqlSession.flush()
        await UniMessage("绑定成功").send()
        

    if setting is None:  # 如果没有设置默认memo
        setting = Setting(user_id=session.id1, default_memo=memo.id)
        sqlSession.add(setting)

    await sqlSession.commit()


@memos.assign("list")
async def list_handler(session: EventSession, sqlSession: async_scoped_session):
    memos = await sqlSession.scalars(select(Memo).where(Memo.user_id == session.id1))

    memos = memos.all()

    if len(memos) == 0:
        return await UniMessage("未绑定任何memos").send()

    datas = []

    for memo in memos:
        try:
            info: dict[Any, Any] = loads(memo.user_info)
            datas.append(
                f"{memo.id}: {memo.url}:\n  用户名: {info.get('username','未知')}\n  昵称: {info.get('nickname','未知')} 身份: {info.get('role','未知')}"
            )
        except Exception as e:
            datas.append(f"{memo.id}: {memo.url}:\n  信息加载失败: {e}")

    await UniMessage("\n".join(datas)).send()


@memos.assign("default")
async def default_handler(memo_id: Match[int], session: EventSession, sqlSession: async_scoped_session):
    setting = await sqlSession.scalar(select(Setting).where(Setting.user_id == session.id1))

    if setting is None:
        return await UniMessage("请先绑定memos").send()

    memo = await sqlSession.scalar(select(Memo).where(Memo.id == memo_id.result).where(Memo.user_id == session.id1))

    if memo is None:
        return await UniMessage("找不到对应memo身份").send()

    setting.default_memo = memo.id

    sqlSession.add(setting)
    await sqlSession.commit()
    await UniMessage("设置成功").send()


@memos.assign("delete")
async def delete_handler(memo_id: Match[int], session: EventSession, sqlSession: async_scoped_session):
    memo = await sqlSession.scalar(select(Memo).where(Memo.id == memo_id.result).where(Memo.user_id == session.id1))

    if memo is None:
        return await UniMessage("找不到对应memo身份").send()

    await sqlSession.delete(memo)
    await sqlSession.commit()
    await UniMessage("删除成功").send()


@memos.assign("create")
async def create_handler(content: Match[str], session: EventSession, sqlSession: async_scoped_session):
    setting = await sqlSession.scalar(select(Setting).where(Setting.user_id == session.id1))

    if setting is None:
        return await UniMessage("请先绑定memos").send()

    memo = await sqlSession.scalar(
        select(Memo).where(Memo.id == setting.default_memo).where(Memo.user_id == session.id1)
    )

    if memo is None:
        return await UniMessage("找不到默认memo").send()

    client = get_client(memo.id, memo.url, memo.token)

    try:
        resp = await client.createMemo(content.result)
        if resp.status_code != 200:
            return await UniMessage("创建失败!").send()
    except Exception as e:
        return await UniMessage(f"创建失败: {e}").send()

    data = resp.json()

    if uid := data.get("uid"):
        await UniMessage(f"创建成功\n{client.buildMemoUrl(uid)}").send(at_sender=True)
    else:
        await UniMessage("创建成功, 但未获取到uid").send(at_sender=True)
