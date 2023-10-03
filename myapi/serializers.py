# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Testperson
from .models import Hochbeet2



class TestpersonSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")  # new

    class Meta:
        model = Testperson
        fields = ('id','name', 'alias', 'rec_time', 'pers_uuid', 'owner')

        #, 'temp_dec','temp_float','temp_char','humidity_dec','humidity_float','humidity_char')

# outdated - delete
class Hochbeet2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hochbeet2
        fields=('rec_time','light','battery','temperature','conductivity','moisture')
