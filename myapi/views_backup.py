from django.shortcuts import render
from rest_framework import viewsets

from .serializers import NetatmoSerializer
from .serializers import Hochbeet2Serializer
from .models import Netatmo
from .models import Hochbeet2

class NetatmoViewSet(viewsets.ModelViewSet):
    queryset=Netatmo.objects.all().order_by('name')
    serializer_class=NetatmoSerializer

class Hochbeet2ViewSet(viewsets.ModelViewSet):
    queryset=Hochbeet2.objects.all().order_by('rec_time')
    serializer_class=Hochbeet2Serializer
# Create your views here.
