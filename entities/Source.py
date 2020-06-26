from app import db
from peewee import *

class Source(Model):
    id = BigIntegerField(primary_key=True)
    source_id = CharField()
    name = CharField()

    class Meta:
        db_table = 'Source'
        database = db