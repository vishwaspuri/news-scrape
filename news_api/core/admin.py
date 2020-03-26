from django.contrib import admin
from .models import Article, State, NationalData
# Register your models here.

admin.site.register(Article)
admin.site.register(State)
admin.site.register(NationalData)

