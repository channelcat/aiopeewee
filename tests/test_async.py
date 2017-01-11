import sys
sys.path.append('/code')

import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s: %(levelname)s: %(message)s")
log = logging.getLogger(__name__)

import asyncio

from peewee import *
import datetime

db = PostgresqlDatabase('testing', host='database', user='admin', password='testpw')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)

class Tweet(BaseModel):
    user = ForeignKeyField(User, related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)

async def main_create():
    print("Start")
    await db.connect()
    await db.create_tables([User, Tweet])
    print("Done")

async def main_users_insert():
    print("Start")
    charlie = await User.create(username='charlizezz')
    print("charlie")
    print(charlie)
    print(charlie.id)
    huey = User(username='hueyzzz')
    await huey.save()
    print("huey")
    print(huey)
    print(huey.id)
    print("Done")

async def main_users_get():
    print("Start")
    charlie = await User.get(User.username == 'charlie')
    print("charlie")
    print(charlie)
    print(charlie.id)
    print("Done")

loop = asyncio.get_event_loop()
#loop.run_until_complete(main_create())
#loop.run_until_complete(main_users_insert())
loop.run_until_complete(main_users_get())