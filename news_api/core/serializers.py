from rest_framework import serializers
from .models import Article,State


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