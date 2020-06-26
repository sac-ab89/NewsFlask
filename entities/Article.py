from app import db
from peewee import *

from entities.Source import Source

class Article(Model):
    id = BigIntegerField(primary_key=True)
    author = CharField()
    content = CharField()
    description = CharField()
    publishedAt = DateTimeField()
    title = CharField()
    URL = CharField()
    urlToImage = CharField()
    source = ForeignKeyField(Source, to_field='id', db_column='source')

    class Meta:
        db_table = 'article'
        database = db