from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TestpersonSerializer
from .serializers import Hochbeet2Serializer
from .models import Testperson
from django_filters.rest_framework import DjangoFilterBackend
from .models import Hochbeet2

class TestpersonViewSet(viewsets.ModelViewSet):
    queryset=Testperson.objects.all().order_by('-rec_time')
    serializer_class=TestpersonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'alias','id']
    search_fields = ['name', 'alias']

class Hochbeet2ViewSet(viewsets.ModelViewSet):
    queryset=Hochbeet2.objects.all().order_by('rec_time')
    serializer_class=Hochbeet2Serializer
# Create your views here.
