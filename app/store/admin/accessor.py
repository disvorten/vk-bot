import typing
from hashlib import sha256
from typing import Optional

from app.base.base_accessor import BaseAccessor
from app.admin.models import Admin

if typing.TYPE_CHECKING:
    from app.web.app import Application


class AdminAccessor(BaseAccessor):
    async def connect(self, app: "Application"):
        self.app = app
        try:
            self.app.database["users"]
        except KeyError:
            self.app.database["users"] = []

    async def get_by_email(self, email: str) -> Optional[Admin]:
        raise NotImplementedError

    async def create_admin(self, email: str, password: str) -> Admin:
        admin = Admin(id=1, email=email, password=password)
        return admin
