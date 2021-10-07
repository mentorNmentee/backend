import peewee as pw
from playhouse.signals import Model

from config import DatabaseInfo

db_info = DatabaseInfo()
db_corn = pw.MySQLDatabase(db_info.database_name, host=db_info.host, port=db_info.port, user=db_info.user, password=db_info.password)


class DatabaseModel(Model):
    class Meta:
        database = db_corn


class UserTable(DatabaseModel):
    class Meta:
        db_table = "user"

    # PK
    id = pw.IntegerField()
    # Login Info
    password = pw.TextField()
    access_token = pw.TextField()
    token_valid_DT = pw.DateTimeField()
    # 개인정보
    email = pw.CharField()
    name = pw.CharField()
    phone_num = pw.CharField()
    gender = pw.CharField()
    birthday = pw.DateField()
    #기타정보
    nickname = pw.CharField()
    # 탈퇴
    delete_request_at = pw.DateTimeField()
    delete_datetime = pw.DateTimeField()
    delte_flag = pw.BooleanField()


class CategoryTable(DatabaseModel):
    class Meta:
        db_table = "interests_category"

    id = pw.IntegerField()
    category_name = pw.CharField()
    category_info = pw.TextField()

class UserCategoryTable(DatabaseModel):
    class Meta:
        db_table = "user_and_category"

    id = pw.IntegerField()
    category_name = pw.CharField()
    category_info = pw.TextField()
