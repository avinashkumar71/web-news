from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=######################'  # here is your API KEY URL
    country = request.GET.get('country')
    category = request.GET.get('category')
    dictt = {}
    dictt['crty'] = 'in'
    request.session['ctry'] = dictt

    if country:
        request.session.get('ctry').clear()
        url_left = 'https://newsapi.org/v2/top-headlines?country='

        url_right = '&apiKey=#########################'  # API KEY
        request.session['ctry'] = country

        url = url_left + country + url_right

    elif request.method == 'POST':
        qvalue = request.POST.get('qvalue')
        url_left = 'https://newsapi.org/v2/top-headlines?q='
        url_right = '&apiKey=###################################'  # API KEY
        url = url_left + qvalue + url_right

    elif category:
        url_left = 'https://newsapi.org/v2/top-headlines?category=' + category
        url_right = '&apiKey=################################'  # API KEY
        url = url_left + url_right

    print(url)
    All_data = requests.get(url).json()
    articles = All_data['articles']
    article = []
    for i in range(len(articles)):
        article.append(articles[i])
    print(article)
    return render(request, 'index.html',
                  {'articles': article, 'category': ['sports', 'science', 'business', 'technology', 'General'], })
