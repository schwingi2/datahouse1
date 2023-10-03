"""myAPI urls.py

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
#router = routers.DefaultRouter()
#router.register(r'Testperson', views.TestpersonViewSet)
#router.register(r'Hochbeet2',views.Hochbeet2ViewSet)

urlpatterns = [
    path('Testperson/', views.TestpersonList.as_view(), name='Testperson-list'),
    path('Testperson/<int:pk>/', views.TestpersonDetail.as_view(), name='Testperson-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
