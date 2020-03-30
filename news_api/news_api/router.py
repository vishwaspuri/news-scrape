from core.viewsets import PageViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
router = DefaultRouter()
router.register(r'Page', PageViewSet)

