from rest_framework import viewsets
from .serializers import PageSerializer
from .models import Page

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serialize(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.data['page_number']=serializer.data['page_number']+1
        serializer.save()
        return Response(serializer.data)
