from django.db import models

# Create your models here.

class Page(models.Model):
    page_number=models.IntegerField(primary_key=True)
    page_name=models.CharField(max_length=100, default='')
    visits = models.IntegerField(default=0)

class Article(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    article_link = models.CharField(max_length=150)
    image_link = models.CharField(max_length=150)
    def __str__(self):
        return self.title

class State(models.Model):
    index=models.IntegerField(primary_key=True)
    state_name=models.CharField(max_length=100)
    india_confirmed_cases=models.IntegerField()
    cured_cases=models.IntegerField()
    deaths_caused=models.IntegerField()

class NationalData(models.Model):
    date=models.DateField()
    number_of_cases=models.IntegerField()
    total_cured=models.IntegerField(default=0)
    total_deaths=models.IntegerField(default=0)


