from celery import shared_task
import wikipedia
from .forms import *
import redis


@shared_task
def search_wikipedia(key, search):
    result = wikipedia.page(search)
    redis_host = redis.Redis(host="localhost", port=6379, db=0)
    wikipedia_search = redis_host.set(key, result.content)
    # result =redis_host.get(wikipedia_search)
    # result = wikipedia.summary(search, sentences=100)
    # return result
