from datetime import datetime
from peewee import RawQuery, Insert
from app import db, app
from entities.Article import Article
from entities.Source import Source
from entities.Source import Source
import json

def post_news(author, content, description, publishedAt, title, URL, URLToImage, source):
    news = Article.create(
        author=author,
        content=content,
        description=description,
        publishedAt=publishedAt,
        title=title,
        URL=URL,
        urlToImage=URLToImage,
        source=source,
    )


def update_source(source_id, name):
    if not (Source.select().where(Source.name.contains(name))):
        source = Source.create(
            source_id=source_id,
            name=name,
        )
    s = Source.get(Source.name == name).id
    return(s)

def get_news():
    news = Article.select().dicts()
    news_list = []
    for item in news:
        author = item['author']
        content = item['content']
        description = item['description']
        publishedAt = item['publishedAt']
        title = item['title']
        URL = item['URL']
        urlToImage = item['urlToImage']
        item['source'] = Source.get(Source.id == item['source']).name
        news_list.append(item)
    return news_list


