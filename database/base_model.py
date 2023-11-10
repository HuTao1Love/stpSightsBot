from peewee import Model, SqliteDatabase
from config import DATABASE_URL


db = SqliteDatabase(DATABASE_URL)


class BaseModel(Model):
    class Meta:
        database = db
