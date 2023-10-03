from django.db import models
import uuid
from pygments.lexers import get_lexer_by_name
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# from pygments
#https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners
#LEXERS = [item for item in get_all_lexers() if item[1]]
#LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
#STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.
# models.py

class Testperson(models.Model):
    pers_uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    rec_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='Testperson', on_delete=models.CASCADE)
    #highlighted = models.TextField()
    class Meta:
        ordering = ['-rec_time']


    #temp_dec = models.DecimalField(max_digits=5, decimal_places=2)
    #temp_float = models.FloatField(max_value=1000, min_value=-1000)
    #temp_char = models.CharField(max_length=60)
    #humidity_dec= models.DecimalField(max_digits=5, decimal_places=2)
    #humidity_float= models.FloatField(max_value=1000, min_value=-1000)
    #humidity_char= models.CharField(max_length=60)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """ 
        Use the `pygments` library to create a highlighted HTML
        representation of the Testperson.
        """
        #lexer = get_lexer_by_name(self.alias)
        options = {'name': self.name} if self.name else {}
       # formatter = HtmlFormatter(style=self.style,
        #                        full=True, **options)
      #  self.highlighted = highlight(self.name)
        super().save(*args, **kwargs)
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