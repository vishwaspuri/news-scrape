from rest_framework import serializers
from .models import Article, State, NationalData, Page


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=(
            'title','description','image_link','article_link'
        )

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields=(
            'state_name','india_confirmed_cases','foreign_confirmed_cases','cured_cases','deaths_caused'
        )

class StateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields=['state_name']

class IndianCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields=[
            'india_confirmed_cases'
        ]

class ForeignCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields=[
            'foreign_confirmed_cases'
        ]

class CuredCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields=[
            'cured_cases'
        ]

class DeathCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields=[
            'deaths_caused'
        ]

class NationalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=NationalData
        fields=(
            'date','number_of_cases','total_cured','total_cured'
        )

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Page
        fields=[
            'page_name'
        ]

class PageViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Page
        fields=(
            'page_name','page_views'
        )