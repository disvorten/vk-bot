from app.admin.models import Admin
from app.web.app import View
from app.web.utils import json_response


class AdminLoginView(View):
    async def post(self):
        data = self.request['data']
        admin = Admin(id=1, email=data['email'], password=data['password'])
        await self.request.app.adminAccessor.create_admin(admin.email, admin.password)
        return json_response()


class AdminCurrentView(View):
    async def get(self):
        raise NotImplementedError
