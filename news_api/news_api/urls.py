"""news_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import TotalPageViews,PageView,ArticleView, StateView, StateNameView, IndianCasesView, ForeignCasesView,CuredCasesView,DeathCasesView,CombinedView,NationalDataView
import core.views as views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news-scrape/', views.news_scrape, name='news_scrape'),
    path('news-scrape/news_result/', ArticleView.as_view(), name='article'),
    path('state-scrape/', views.StateData, name='state_scrape'),
    path('state-scrape/state_result/', StateView.as_view(), name='state'),
    path('state-name/', StateNameView.as_view(), name='state name'),
    path('indian-cases/', IndianCasesView.as_view(), name='indian cases'),
    path('foreign-cases/', ForeignCasesView.as_view(), name='foreign cases'),
    path('cured-cases/', CuredCasesView.as_view(), name='cured cases'),
    path('dead-cases/', DeathCasesView.as_view(), name='dead cases'),
    path('combo-mode/', CombinedView.as_view(), name='combined info'),
    path('national-data/', NationalDataView.as_view(), name='national data'),
    path('post-view/', PageView.as_view(), name='add click'),
    path('page-info/', TotalPageViews.as_view(), name='page-data'),
]
