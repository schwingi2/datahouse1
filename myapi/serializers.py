# serializers.py
from rest_framework import serializers
from .models import Testperson
from .models import Hochbeet2


class TestpersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Testperson
        fields = ('id','name', 'alias', 'rec_time', 'pers_uuid')

        #, 'temp_dec','temp_float','temp_char','humidity_dec','humidity_float','humidity_char')


class Hochbeet2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hochbeet2
        fields=('rec_time','light','battery','temperature','conductivity','moisture')
