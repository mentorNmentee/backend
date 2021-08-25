import datetime

import bcrypt
import jwt

from database.user_db import UserHelper


class UserManager:
    def __init__(self):
        self.user_helper = UserHelper()

    def password_check(self, password, row_data):
        return bcrypt.checkpw(password.encode(), row_data.password.encode())

    def deactivate_check(self, row_data):
        if row_data.deactivate_DT is not None:
            if row_data.delete_DT < datetime.datetime.utcnow():
                row_data.delete()
                return True
            else:
                return True
        else:
            return False

    def hash_password(self, password):
        salt = bcrypt.gensalt(10)
        return bcrypt.hashpw(password.encode(), salt)

    def token_create(self, row_data):
        row_data.access_token = jwt.encode({"user_id": row_data.user_id}, "mentorNmenteeBackend", algorithm="HS256")
        row_data.token_valid_DT = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        return row_data.save()

    def sign_up(self, data):
        temp = self.user_helper.user_id_check(data.user_id)
        if temp:
            if self.deactivate_check(temp):
                return 400, {"message": "This is Deactivate Account ID"}
            return 400, {"message": "ID already in use"}
        elif self.user_helper.email_check(data.email):
            return 400, {"message": "Email already in use"}
        elif self.user_helper.phone_num_check(data.phone_num):
            return 400, {"message": "Phone Num already in use"}
        else:
            data_dict = data.dict()
            data_dict["password"] = self.hash_password(data.password)
            self.user_helper.create_user(data_dict)
            return 201, {"message": "SignUp Success"}

    def login(self, data):
        row_data = self.user_helper.user_id_check(data.user_id)
        if row_data is not None:
            if self.password_check(data.password, row_data):
                if self.deactivate_check(row_data):
                    return 400, {"message": "Deactivate Account"}
                else:
                    self.token_create(row_data)
                    return 200, {"token": row_data.access_token}
            else:
                return 400, {"message": "Please Check Password"}
        else:
            return 400, {"message": "Please Check ID"}

    def logout(self, access_token):
        row_data = self.user_helper.token_check(access_token)
        if row_data is not None:
            row_data.access_token = None
            row_data.token_valid_DT = None
            row_data.save()
            return 200, {"message": "Logout Success"}
        else:
            return 400, {"message": "Invalid Token"}

    def edit_user(self, data):
        row_data = self.user_helper.token_check(data.access_token)
        if row_data is not None:
            row_data.name = data.name
            row_data.email = data.email
            row_data.phone_num = data.phone_num
            row_data.sex = data.sex
            row_data.birthday = data.birthday
            row_data.nickname = data.nickname
            row_data.save()
            return 200, {"message": "Edit User Information Success"}
        else:
            return 400, {"message": "Invalid Token"}

    def edit_interests(self, data):
        row_data = self.user_helper.token_check(data.access_token)
        if row_data is not None:
            row_data.category1 = data.category1
            row_data.category2 = data.category2
            row_data.category3 = data.category3
            row_data.category4 = data.category4
            row_data.category5 = data.category5
            row_data.save()
            return 200, {"message": "Edit Interests Category Information Success"}
        else:
            return 400, {"message": "Invalid Token"}

    def change_password(self, data):
        row_data = self.user_helper.token_check(data.access_token)
        if row_data is not None:
            row_data.password = self.hash_password(data.password)
            row_data.save()
            return 200, {"message": "Change Password Success"}
        else:
            return 400, {"message": "Invalid Token"}