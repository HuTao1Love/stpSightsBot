from peewee import BigIntegerField, TextField, DateField, CharField, ForeignKeyField, DoubleField, BooleanField
from .base_model import BaseModel
from view import formatted


class LocationType(BaseModel):
    class Meta:
        table_name = 'location_types'

    id = BigIntegerField(column_name="id", primary_key=True)
    name = CharField(column_name="name", max_length=30)


class Location(BaseModel):
    class Meta:
        table_name = 'locations'

    id = BigIntegerField(column_name="id", primary_key=True)
    name = CharField(column_name="name", max_length=30)
    type = ForeignKeyField(LocationType, to_field="id")
    description = TextField(column_name="description")
    created = DateField(column_name="created")
    photo = TextField(column_name="photo_url")
    latitude = DoubleField(column_name="latitude")
    longitude = DoubleField(column_name="longitude")

    def get_text(self) -> str:
        return formatted.LOCATION_VIEW.format(name=self.name, type=self.type.name, description=self.description, created=self.created)

    def url_yandex(self) -> str:
        return formatted.MAP_LOCATION_YANDEX.format(latitude=self.latitude, longitude=self.longitude)

    def url_google(self) -> str:
        return formatted.MAP_LOCATION_GOOGLE.format(latitude=self.latitude, longitude=self.longitude)


class User(BaseModel):
    class Meta:
        table_name = 'users'

    id = BigIntegerField(column_name='id', primary_key=True)
    is_admin = BooleanField(column_name='is_admin', default=False)
