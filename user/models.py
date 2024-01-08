from tortoise.models import Model
from tortoise import fields
from tortoise import Tortoise

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(200,pk=False)
    email = fields.CharField(200,pk=False)
    phone = fields.IntField(pk=False)
    password = fields.CharField(200,pk=False)


class Person(Model):
    id = fields.IntField(pk =True)
    name = fields.CharField(200,pk=False)
    email = fields.CharField(200,pk=False)
    phone = fields.IntField(pk=False)
    password = fields.CharField(200,pk=False)



Tortoise.init_models(['user.models'],'models')    