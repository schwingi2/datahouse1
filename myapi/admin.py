from django.contrib import admin

# Register your models here.
from .models import Testperson
from .models import Hochbeet2
admin.site.register(Testperson)
admin.site.register(Hochbeet2)