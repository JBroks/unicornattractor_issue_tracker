from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.date_joined