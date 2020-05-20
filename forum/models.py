from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count

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
        return "Forum post #{0} [{1}] added by {2}".format(
            self.id, self.subject, self.user.username)
            
    def latest_comment_date(self):
        return self.post_comments.latest('date_updated').date_updated
    
    def comments_count(self):
        return CommentPost.objects.annotate(Count('comment')).count()

class CommentPost(models.Model):
    '''
    Enables users to comment on a given forum post, express their opinions,
    and be a part of the community
    '''
    
    post = models.ForeignKey(
        Post,
        related_name='post_comments',
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
        return "Comment #{0} added by {1} for post #{2}".format(
            self.id, self.user.username, self.post.id)