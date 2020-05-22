from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count

# Create your models here.
class Thread(models.Model):
    '''
    Enable user to create a thread (first post that starts a discussion/topic)
    on the forum
    Auto_now_add used to add date and time when the thread was created, 
    and auto_now used to add date and time when thread was updated / edited.
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
        return "Forum thread #{0} [{1}] added by {2}".format(
            self.id, self.subject, self.user.username)
    
    def latest_post_date(self):
        return self.forum_post.latest('date_updated').date_updated
    
    def latest_post_author(self):
        return self.forum_post.latest('user').user
        
    def post_count(self):
        return self.forum_post.annotate(Count('post')).count()
    
    def get_total_likes(self):
        return self.likes.users.count()

    def get_total_dis_likes(self):
        return self.dis_likes.users.count()
    
class Post(models.Model):
    '''
    Enables users to comment on a given forum thread, express their opinions,
    and be a part of the community
    '''
    
    thread = models.ForeignKey(
        Thread,
        related_name='forum_post',
        null=True,
        on_delete=models.CASCADE)
    
    user = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.CASCADE)
        
    post = models.TextField(
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
        return "Post #{0} added by {1} for thread #{2}".format(
            self.id, self.user.username, self.thread.id)

class Like(models.Model):
    ''' Enables user to like a posted thread '''

    thread = models.OneToOneField(
        Thread, 
        related_name="thread_likes",
        on_delete=models.CASCADE
        )
        
    user = models.ManyToManyField(
        User, 
        related_name='thread_likes_users'
        )
        
    date_created = models.DateTimeField(
        auto_now_add=True
        )
        
    date_updated = models.DateTimeField(
        auto_now=True
        )

    def __str__(self):
         return str(self.thread.thread)[:30]

class Dislike(models.Model):
    ''' Enables user to dislike a posted thread '''

    thread = models.OneToOneField(
        Thread, 
        related_name="thread_dislikes",
        on_delete=models.CASCADE
        )
        
    user = models.ManyToManyField(
        User, 
        related_name='thread_dislikes_users'
        )
        
    date_created = models.DateTimeField(
        auto_now_add=True
        )
        
    date_updated = models.DateTimeField(
        auto_now=True
        )

    def __str__(self):
         return str(self.thread.thread)[:30]
