# Create your views here.
from .models import Testperson
from .serializers import TestpersonSerializer
from rest_framework import generics, permissions
from rest_framework.decorators import api_view  
from rest_framework.response import Response  
from rest_framework.reverse import reverse  

from .permissions import IsOwnerOrReadOnly

@api_view(["GET"])  # new
def api_root(request, format=None):
    return Response(
        {
            "Testperson": reverse("Testperson-list", request=request, format=format),
        }
    )


class TestpersonList(generics.ListCreateAPIView):
    queryset = Testperson.objects.all()
    serializer_class = TestpersonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):  # new
        serializer.save(owner=self.request.user)


class TestpersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testperson.objects.all()
    serializer_class = TestpersonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)