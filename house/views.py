import django_filters
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from house.models import House, HouseType
from house.serializer import HouseSerializer, HouseTypeSerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = []
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'], url_path='upload-photo')
    def upload_photo(self, request, pk=None):
        house = self.get_object()
        file = request.FILES['file']
        house.image = file
        house.save()
        return Response({"message": "Upload successfully"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='client/get-houses')
    def get_houses(self, request):
        best_offer = House.objects.filter(is_best_offer=True)
        recent = House.objects.filter(is_best_offer=False)
        context = {
            "best_offer": self.get_serializer(best_offer, many=True).data,
            "recent": self.get_serializer(recent, many=True).data
        }
        return Response(context, status=status.HTTP_200_OK)


class HouseTypeViewSet(viewsets.ModelViewSet):
    queryset = HouseType
    serializer_class = HouseTypeSerializer
    permission_classes = []