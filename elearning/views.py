from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'elearning/index.php')

def contact(request):
	return render(request,'elearning/basic.html',{'content':['Test block content on elearning','test 1.2.3.']})
	
