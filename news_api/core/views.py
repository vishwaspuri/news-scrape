from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article,State
from .serializers import ArticleSerializer, StateSerializer,StateNameSerializer, IndianCasesSerializer,ForeignCasesSerializer, CuredCasesSerializer,DeathCasesSerializer
from bs4 import BeautifulSoup as Soup
import requests

# Create your views here.
def news_scrape(request):
    Article.objects.all().delete()
    session=requests.Session()
    url='https://www.hindustantimes.com/topic/coronavirus'
    content=session.get(url,verify=False).content
    soup=Soup(content, 'lxml')
    title = []
    link = []
    description = []
    image_link = []
    imgUrl = []

    for element in soup.find_all(class_="authorListing"):

        for Desc in element.find_all(class_='para-txt'):
            link.append(Desc.a['href'])
            description.append(Desc.text)

        for Title in element.find_all(class_='media-heading headingfour'):
            title.append(Title.a['title'])

        for list_images in element.find_all(class_='media-img'):
            imgUrl.append(list_images.a.img['src'])

    for i in range(0,len(imgUrl)-1):
        new_article = Article()
        new_article.image_link = imgUrl[i]
        new_article.title = title[i]
        new_article.article_link = link[i]
        new_article.description = description[i]
        new_article.save()

    return redirect('news_result/')

def StateData(request):
#   State.objects.all().delete()
    session = requests.Session()
    url = 'https://www.mohfw.gov.in/'
    content = session.get(url, verify=False).content
    soup = Soup(content, 'lxml')
    index = []
    StateName = []
    confirmed_cases_indian = []
    confirmed_cases_foreign = []
    cured = []
    deaths = []

    table_class = soup.find_all(class_='table table-striped table-dark')[7]
    i = 0
    for element in table_class.find_all('tr'):
        if i < 27:
            table_row = element.find_all('td')
            x = 0
            for td in table_row:
                if x == 0:
                    index.append(int(td.string))
                    x = x + 1
                elif x == 1:
                    StateName.append(td.string)
                    x = x + 1
                elif x == 2:
                    confirmed_cases_indian.append(int(td.string))
                    x = x + 1
                elif x == 3:
                    confirmed_cases_foreign.append(int(td.string))
                    x = x + 1
                elif x == 4:
                    cured.append(int(td.string))
                    x = x + 1
                elif x == 5:
                    deaths.append(int(td.string))
                    x = x + 1
            i = i + 1
    for i in range(0,26):
        new_state=State()
        new_state.state_name=StateName[i]
        new_state.india_confirmed_cases=confirmed_cases_indian[i]
        new_state.foreign_confirmed_cases=confirmed_cases_foreign[i]
        new_state.cured_cases=cured[i]
        new_state.deaths_caused=deaths[i]
        new_state.save()
    return redirect('state_result/')


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        qs=Article.objects.all()
        serializer=ArticleSerializer(qs,many=True)
        return Response(serializer.data)


class StateView(APIView):
    def get(self, request, *args, **kwargs):
        qs=State.objects.all()
        serializer=StateSerializer(qs,many=True)
        return Response(serializer.data)

class StateNameView(APIView):
    def get(self, request, *args, **kwargs):
        qs=State.objects.all()
        serializer=StateNameSerializer(qs,many=True)
        return Response(serializer.data)

class IndianCasesView(APIView):
    def get(self, request, *args, **kwargs):
        qs=State.objects.all()
        serializer=IndianCasesSerializer(qs,many=True)
        return Response(serializer.data)

class ForeignCasesView(APIView):
    def get(self, request, *args, **kwargs):
        qs=State.objects.all()
        serializer=ForeignCasesSerializer(qs,many=True)
        return Response(serializer.data)

class CuredCasesView(APIView):
    def get(self, request, *args, **kwargs):
        qs=State.objects.all()
        serializer=CuredCasesView(qs,many=True)
        return Response(serializer.data)

class DeathCasesView(APIView):
    def get(self, request, *args, **kwargs):
        qs=State.objects.all()
        serializer=DeathCasesSerializer(qs,many=True)
        return Response(serializer.data)