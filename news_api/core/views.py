from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article,State, NationalData, Page
from .serializers import PageSerializer,ArticleSerializer, StateSerializer,StateNameSerializer, IndianCasesSerializer,ForeignCasesSerializer, CuredCasesSerializer,DeathCasesSerializer,NationalDataSerializer
from bs4 import BeautifulSoup as Soup
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.http import JsonResponse
from .secrets import GOOGLE_CREDENTIALS
import json

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
            try:
                imgUrl.append(list_images.a.img['data-src'])
            except:
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
    State.objects.all().delete()
    session = requests.Session()
    url = 'https://www.mohfw.gov.in/'
    content = session.get(url, verify=False).content
    soup = Soup(content, 'lxml')
    index=[]
    state_name=[]
    confirmed_cases_indian=[]
    cured=[]
    deaths=[]
    i=0
    table=soup.find_all('table',{'class':'table table-striped'})[0]
    for element in table.find_all('tr'):
        if i>0 and i<31:
            table_row=element.find_all('td')
            index.append(int(table_row[0].string))
            state_name.append(table_row[1].string)
            confirmed_cases_indian.append(int(table_row[2].string))
            cured.append(int(table_row[3].string))
            deaths.append(int(table_row[4].string))
        i=i+1

    newState = State()
    newState.index = 30
    newState.state_name = 'India'
    india_confirmed_cases=0
    india_cured_cases=0
    india_total_deaths=0
    for i in range(0,30):
        new_state=State()
        new_state.index=index[i]
        new_state.state_name=state_name[i]
        new_state.india_confirmed_cases=confirmed_cases_indian[i]
        new_state.cured_cases=cured[i]
        new_state.deaths_caused=deaths[i]
        new_state.save()
        india_confirmed_cases=confirmed_cases_indian[i]+india_confirmed_cases
        india_cured_cases=cured[i]+india_cured_cases
        india_total_deaths=deaths[i]+india_total_deaths
    newState.india_confirmed_cases=india_confirmed_cases
    newState.cured_cases=india_cured_cases
    newState.deaths_caused=india_total_deaths
    newState.save()
    return redirect('/state-result/')

    new_state=State()
    news_state.index=30
    new_state.state_name='India'

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
        serializer=CuredCasesSerializer(qs,many=True)
        return Response(serializer.data)

class DeathCasesView(APIView):
    def get(self, request, *args, **kwargs):
        qs=State.objects.all()
        serializer_one=DeathCasesSerializer(qs,many=True)
        return Response(serializer_one.data)

class CombinedView(APIView):
    def get(self, request, *args, **kwargs):
        qs = State.objects.all()
        serializer_one = StateNameSerializer(qs, many=True)
        serializer_two = IndianCasesSerializer(qs, many=True)
        serializer_three = ForeignCasesSerializer(qs, many=True)
        serializer_four = CuredCasesSerializer(qs, many=True)
        serializer_five = DeathCasesSerializer(qs, many=True)
        return Response([serializer_one.data,serializer_two.data,serializer_three.data, serializer_four.data,serializer_five.data])


class NationalDataView(APIView):
    def get(self, request, *args, **kwargs):
        qs=NationalData.objects.all()
        serializer=NationalDataSerializer(qs,many=True)
        return Response(serializer.data)

def hitcount(request, pk=None):
    page = Page.objects.get(pk=pk)
    page.visits = page.visits+1
    page.save()
    return redirect('/hits/')

class HitCountView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Page.objects.all()
        serializer = PageSerializer(qs, many=True)
        return Response(serializer.data)

def DistrictwiseData(request):
    scope = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file',
             'https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_dict(GOOGLE_CREDENTIALS, scope)
    client = gspread.authorize(creds)
    sheet = client.open("District Data").sheet1
    data = sheet.get_all_values()
    data_list = []
    for element in data:
        data_dict = {
            "State": element[0],
            "District": element[1],
            "Num_cases_in_district": element[2]
        }
        data_list.append(data_dict)
    return JsonResponse(data_list, safe=False)