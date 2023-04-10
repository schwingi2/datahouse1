from django.db import models
import uuid

# Create your models here.
# models.py
class Testperson(models.Model):
    pers_uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    rec_time = models.DateTimeField(auto_now_add=True)



    #temp_dec = models.DecimalField(max_digits=5, decimal_places=2)
    #temp_float = models.FloatField(max_value=1000, min_value=-1000)
    #temp_char = models.CharField(max_length=60)
    #humidity_dec= models.DecimalField(max_digits=5, decimal_places=2)
    #humidity_float= models.FloatField(max_value=1000, min_value=-1000)
    #humidity_char= models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Hochbeet2(models.Model):
    #name = models.CharField(max_length=60)
    #alias = models.CharField(max_length=60)
    #light = models.DecimalField(max_digits=5, decimal_places=1)
    rec_time = models.DateTimeField(auto_now_add=True)
    light = models.CharField(max_length=15)
    battery= models.CharField(max_length=15)
    temperature = models.CharField(max_length=15)
    conductivity=models.CharField(max_length=15)
    moisture=models.CharField(max_length=15)

    def __str__(self):
        return self.rec_time.name