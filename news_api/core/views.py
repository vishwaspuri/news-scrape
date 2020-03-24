from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from bs4 import BeautifulSoup as Soup
import requests

# Create your views here.
def scrape(request):
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

    return redirect('scrape_result/')






class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        qs=Article.objects.all()
        serializer=ArticleSerializer(qs,many=True)
        return Response(serializer.data)
