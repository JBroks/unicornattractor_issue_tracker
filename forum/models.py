from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    '''
    Enable user to submit a post on the forum
    Auto_now_add used to add date and time when post was created, and auto_now
    used to add date and time when post was updated / edited.
    '''
    
    user = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.CASCADE)
    
    subject = models.CharField(
        max_length=100,
        blank=False)
        
    description = models.TextField(
        max_length=30000,
        blank=False)
        
    date_created = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True)
        
    date_updated = models.DateTimeField(
        blank=False,
        null=False,
        auto_now=True,
        )
        
    class Meta:
        ordering = ['-id']
        
    def __str__(self):
        return "Forum post #{0} [{1}] by {2}".format(
            self.id, self.subject, self.user)