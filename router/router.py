from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from src.user import UserManager

router = APIRouter()
user_manager = UserManager()


class SignUpInfo(BaseModel):
    user_id: str
    password: str
    name: str
    email: str
    phone_num: str
    sex: str
    birthday: str
    nickname: str


class LoginInfo(BaseModel):
    user_id: str
    password: str


class EditUserInfo(BaseModel):
    access_token: str
    name: str
    email: str
    phone_num: str
    sex: str
    birthday: str
    nickname: str


class EditInterestsInfo(BaseModel):
    access_token: str
    category1: str
    category2: str
    category3: str
    category4: str
    category5: str


class ChangePasswordINfo(BaseModel):
    access_token: str
    password: str


@router.post("/SignUp/")
def sign_up_user(sign_up_info: SignUpInfo):
    code, content = user_manager.sign_up(sign_up_info)
    return JSONResponse(status_code=code, content=content)


@router.post("/Login/")
def login_user(login_info: LoginInfo):
    code, content = user_manager.login(login_info)
    return JSONResponse(status_code=code, content=content)


@router.post("/Logout/")
def logout_user(access_token):
    code, content = user_manager.logout(access_token)
    return JSONResponse(status_code=code, content=content)


@router.post("/EditUser/")
def edit_user(edit_user_info: EditUserInfo):
    code, content = user_manager.edit_user(edit_user_info)
    return JSONResponse(status_code=code, content=content)


@router.post("/EditInterests/")
def edit_interests(edit_interests_info: EditInterestsInfo):
    code, content = user_manager.edit_interests(edit_interests_info)
    return JSONResponse(status_code=code, content=content)


@router.post("/ChangePassword/")
def change_password(change_password_info: ChangePasswordINfo):
    code, content = user_manager.change_password(change_password_info)
    return JSONResponse(status_code=code, content=content)
