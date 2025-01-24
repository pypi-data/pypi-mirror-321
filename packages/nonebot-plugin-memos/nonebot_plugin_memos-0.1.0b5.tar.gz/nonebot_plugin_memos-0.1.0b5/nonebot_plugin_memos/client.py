from httpx import AsyncClient, Response
from yarl import URL


class ApiClient:
    def __init__(self, base_url: str, token: str):
        self.base_url: URL = URL(base_url)
        self.client: AsyncClient = AsyncClient(
            headers={"Authorization": f"Bearer {token}"}
        )
        self.raw_data: list[str] = [base_url, token]

    def update_raw_data(self, base_url: str, token: str):
        if self.raw_data != [base_url, token]:
            self.base_url = URL(base_url)
            self.client.headers["Authorization"] = f"Bearer {token}"
            self.raw_data = [base_url, token]

    async def getAuthStatus(self, token: str | None = None) -> Response:
        return await self.client.post(
            str(self.base_url / "api/v1/auth/status"),
            headers={
                "Authorization": f"Bearer {token}"
                if token
                else self.client.headers.get("Authorization")
            },
        )

    async def checkAuthStatus(self, token: str | None = None) -> bool:
        try:
            response = await self.getAuthStatus(token)
            return response.status_code == 200
        except Exception:
            return False

    async def createMemo(
        self, content: str, visibility: str = "VISIBILITY_UNSPECIFIED"
    ) -> Response:
        return await self.client.post(
            str(self.base_url / "api/v1/memos"),
            json={"content": content, "visibility": visibility},
        )

    def buildMemoUrl(self, memo_id: int) -> str:
        return str(self.base_url / f"m/{memo_id}")
