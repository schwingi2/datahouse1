from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>HEY THERE THIS IS A TEST OF ALTERING VIEWS.PY</h2>")