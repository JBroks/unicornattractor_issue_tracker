from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count

# Create your models here.


class Ticket(models.Model):
    '''
    Enable user to submit a ticket with a choice of a ticket type
    (bug or feature).
    Status choice - default status will be set to "Open" and admin will be able
    update it.
    Auto_now_add used to add date and time when ticket was created,
    and auto_now used to add date and time when ticket was updated / edited.
    '''
    TYPE_CHOICES = (
        ('Bug', 'Bug'),
        ('Feature', 'Feature'),
        )
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Closed', 'Closed'),
        )
    
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    ticket_type = models.CharField(
        max_length=7,
        choices=TYPE_CHOICES)
    ticket_status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES)
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
        return 'Ticket #{0} [{1}] {2} - {3}'.format(
            self.id, self.ticket_status, self.ticket_type, self.subject)
    
    def tickets_upvotes_count(self):
        return self.upvote_ticket_key.annotate(num_upvotes=Count('id')).count()


class Upvote(models.Model):
    '''
    Enables users to upvote any ticket
    '''
    ticket = models.ForeignKey(
        Ticket,
        related_name='upvote_ticket_key',
        null=True,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    date_created = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True)
    
    def __str__(self):
        return 'Ticket #{0} upvoted by {1}'.format(
            self.ticket.id, self.user.username)

            
class Donation(models.Model):
    '''
    Enables users to donate an amount of their choice in order to prioritise
    development of any feature.
    '''
    ticket = models.ForeignKey(
        Ticket,
        null=True,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    donation_amount = models.IntegerField(
        blank=False,
        default=0)
    date_created = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True)
    
    def __str__(self):
        return '€{0} donated by {1} for ticket #{2}'.format(
            self.donation_amount, self.user.username, self.ticket.id)

            
class Comment(models.Model):
    '''
    Enables users to comment on a given ticket, put forward their suggestion
    and ideas on how to fix an issue, or just express their opinions.
    '''
    ticket = models.ForeignKey(
        Ticket,
        null=True,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    comment = models.TextField(
        max_length=8000,
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
        ordering = ['-date_created']
        
    def __str__(self):
        return 'Comment #{0} added by {1} for ticket #{2}'.format(
            self.id, self.user.username, self.ticket.id)
