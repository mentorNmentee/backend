import datetime

from database import *


class UserHelper:
    def __init__(self):
        pass

    def user_id_check(self, user_id):
        return UserTable.get_or_none(UserTable.user_id == user_id)

    def token_check(self, access_token):
        row_data = UserTable.get_or_none(UserTable.access_token == access_token)
        if row_data is not None:
            if row_data.token_valid_DT > datetime.datetime.utcnow():
                return row_data
        return None

    def email_check(self, email):
        return UserTable.get_or_none(UserTable.email == email)

    def phone_num_check(self, phone_num):
        return UserTable.get_or_none(UserTable.phone_num == phone_num)

    def nickname_check(self, nickname):
        return UserTable.get_or_none(UserTable.nickname == nickname)

    def create_user(self, data):
        return UserTable.create(**data)