# Create your views here.
from .models import Testperson
from .serializers import TestpersonSerializer
from rest_framework import generics


class TestpersonList(generics.ListCreateAPIView):
    queryset = Testperson.objects.all()
    serializer_class = TestpersonSerializer


class TestpersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testperson.objects.all()
    serializer_class = TestpersonSerializer