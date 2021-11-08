from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from src.user import UserManager

router = APIRouter()
user_manager = UserManager()


class SignUpInfo(BaseModel):
    email: str
    password: str
    name: str
    phone_num: str
    gender: str
    birthday: str
    nickname: str


class LoginInfo(BaseModel):
    email: str
    password: str


class EditUserInfo(BaseModel):
    access_token: str
    name: str
    email: str
    phone_num: str
    gender: str
    birthday: str
    nickname: str


class EditInterestsInfo(BaseModel):
    access_token: str
    category1: str
    category2: str
    category3: str
    category4: str
    category5: str


class ChangePasswordInfo(BaseModel):
    access_token: str
    password: str

class SingUpSuccessResponse(BaseModel):
    access_token: str

class LoginSuccessResponse(BaseModel):
    id: int = 3
    password: str = "$2b$10$uA.Q/6/2sws0a/4FFX4lX.zs64keU2G.zQURzCrm7JGwO2PdBTHoW"
    access_token: str = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRzZXQifQ.kaDzCP0Wg9fOeVx7zLzVJCaniIzBbVttTghV9zGaCEs",
    token_valid_datetime: str = "2021-11-09T16:19:06",
    email: str = "test@test.com",
    name: str = "용은재",
    phone_num: str = "01030754036",
    gender: str = "F",
    birthday: str = "2020-01-01",
    nickname: str = "은재",
    delete_request_at: str = None,
    delete_datetime: str = None,
    delete_flag: bool = False

@router.post("/sign-up/")
def sign_up_user(sign_up_info: SignUpInfo):
    """
    ## 유저 회원가입 엔드포인트
    ```python
    # Parameters (JSON - BODY)
    ----------
    email: str # 유저 이메일
    password: str # 비밀번호
    check_password: str # 비밀번호 체크
    name: str # 유저 이름
    gender: str # 유저 성별 F or M
    birthday: str # 유저 생일 'YYYY-MM-DDTHH:MM:SS' 형식 유지
    nickname: str # 유저 닉네임
    phone_num: int = None # 유저 핸드폰 번호
    -------
    ```

    """
    code, content = user_manager.sign_up(sign_up_info)
    return JSONResponse(status_code=code, content=content)


@router.post("/login/", response_model=LoginSuccessResponse)
def login_user(login_info: LoginInfo):
    """
        ## 유저 회원가입 엔드포인트
        ```python
        # Parameters (JSON - BODY)
        ----------
        email: str # 유저 이메일
        password: str # 비밀번호
        -------
        ```
    """
    code, content = user_manager.login(login_info)
    return content


@router.post("/logout/")
def logout_user(access_token):
    code, content = user_manager.logout(access_token)
    return JSONResponse(status_code=code, content=content)


@router.put("/edit-user/")
def edit_user(edit_user_info: EditUserInfo):
    code, content = user_manager.edit_user(edit_user_info)
    return JSONResponse(status_code=code, content=content)


@router.post("/edit-interests/")
def edit_interests(edit_interests_info: EditInterestsInfo):
    code, content = user_manager.edit_interests(edit_interests_info)
    return JSONResponse(status_code=code, content=content)


@router.put("/change-password/")
def change_password(change_password_info: ChangePasswordInfo):
    code, content = user_manager.change_password(change_password_info)
    return JSONResponse(status_code=code, content=content)
