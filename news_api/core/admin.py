from django.contrib import admin
from .models import Article, State, Page, NationalData

# Register your models here.

admin.site.register(Article)
admin.site.register(State)
admin.site.register(Page)
admin.site.register(NationalData)

