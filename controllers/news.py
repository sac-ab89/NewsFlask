from flask import Blueprint
from flask import request
import json
import requests
from services import news_service

news = Blueprint('news', __name__)

url = ('https://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey=')

url += 'f4b8ad7a65494c0cb91ec34ffbc6c89e'


@news.route('/api/fetch-news',methods=['GET','POST'])
def fetch_news():
    """Method to fetch the news """
    try:
        news = requests.get(url)
        news_json = json.loads(news.text)
        for i in range(0, len(news_json)):
            source = news_service.update_source(
                source_id=news_json["articles"][i]["source"]["id"],
                name=news_json["articles"][i]["source"]["name"]
            )
            news_post = news_service.post_news(
                author = news_json["articles"][i]['author'],
                content = news_json["articles"][i]['content'],
                description = news_json["articles"][i]['description'],
                publishedAt = news_json["articles"][i]['publishedAt'],
                title = news_json["articles"][i]['title'],
                URL = news_json["articles"][i]['url'],
                URLToImage = news_json["articles"][i]['urlToImage'],
                source = source,
            )
        return 'OK'
    except Exception:
        raise('Server error')

@news.route('/api/list-news',methods=['GET'])
def list_news():
    try:
        news = news_service.get_news()
        return news
    except Exception:
        raise('Server error')
