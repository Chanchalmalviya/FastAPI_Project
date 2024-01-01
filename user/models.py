from tortoise.models import Model
from tortoise import fields
from tortoise import Tortoise

class User(Model):
    id = fields.IntField()
    name = fields.CharField(200)
    email = fields.CharField(200)
    phone = fields.IntField(10)
    password = fields.CharField(200)


Tortoise.init_models(['user.models'],'models')    