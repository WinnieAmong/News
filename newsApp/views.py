from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):
    newsApi = NewsApiClient(api_key = 'eda2ee1984334913acb793c1ca3a3446')
    headlines = newsApi.get_top_headlines(sources = 'bbc_news')
    articles = headlines['articles']
    desc = []
    news = []
    image = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        image.append(article['urlToImage'])

    mylist= zip(desc,news,image)


    return render ('index.html', context= {'mylist': mylist})
