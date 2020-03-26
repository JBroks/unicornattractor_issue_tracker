from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Ticket(models.Model):
    '''
    
    '''
    TYPE_CHOICES = (
        ("B", "Bug"),
        ("F", "Feature"),
        )
    
    STATUS_CHOICES = (
        ("OP", "Open"),
        ("IP", "In Progres"),
        ("CO", "Completed"),
        ("CL", "Closed"),
        )
    
    user_id = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.CASCADE)
        
    ticket_type = models.CharField(
        max_length=1, 
        choices=TYPE_CHOICES)
        
    ticket_status = models.CharField(
        max_length=2, 
        choices=STATUS_CHOICES)
    
    subject = models.CharField(
        max_length=100,
        blank=False)
        
    description = models.TextField(
        max_length=3000,
        blank=False)
        
    date_created = models.DateTimeField(
        auto_now_add=True)
        
    date_updated = models.DateTimeField(
        auto_now=True)
        
    def __str__(self):
        return "#{0} [{1} - {2}] - {3}".format(
            self.id, self.ticket_type, self.ticket_status, self.title)
        
    