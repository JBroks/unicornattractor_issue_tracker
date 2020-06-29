from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count

# Create your models here.


class Thread(models.Model):
    '''
    Enable user to create a thread (first post that starts a discussion/topic)
    on the forum.
    Auto_now_add used to add date and time when the thread was created,
    and auto_now used to add date and time when thread was updated / edited.
    '''
    user = models.ForeignKey(
        User,
        related_name='thread_author_key',
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
        db_table = 'thread'
        ordering = ['-id']
        
    def __str__(self):
        return 'Forum thread #{0} [{1}] added by {2}'.format(
            self.id, self.subject, self.user.username)
    
    def latest_post_date(self):
        return self.post_thread_key.latest('date_updated').date_updated
    
    def latest_post_author(self):
        return self.post_thread_key.latest('user').user
        
    def post_count(self):
        return self.post_thread_key.annotate(Count('post')).count()
    
    def thread_likes_count(self):
        return self.thread_vote_thread_key.filter(
            vote_type='like').annotate(Count('vote_type')).count()
    
    def thread_dislikes_count(self):
        return self.thread_vote_thread_key.filter(
            vote_type='dislike').annotate(Count('vote_type')).count()


class Post(models.Model):
    '''
    Enables users to comment on a given forum thread, express their opinions,
    and be a part of the community.
    '''
    thread = models.ForeignKey(
        Thread,
        related_name='post_thread_key',
        null=True,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        related_name='post_author_key',
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
        db_table = 'post'
        ordering = ['-date_created']
        
    def __str__(self):
        return 'Post #{0} added by {1} for thread #{2}'.format(
            self.id, self.user.username, self.thread.id)
    
    def post_likes_count(self):
        return self.post_vote_post_key.filter(
            vote_type='like').annotate(Count('vote_type')).count()
        
    def post_dislikes_count(self):
        return self.post_vote_post_key.filter(
            vote_type='dislike').annotate(Count('vote_type')).count()
    
    def post_voters(self):
        return self.post_vote_post_key.values_list('user', flat=True)


class ThreadVote(models.Model):
    '''
    Enables users to like/dislike thread.
    '''
    thread = models.ForeignKey(
        Thread,
        related_name='thread_vote_thread_key',
        null=True,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        related_name='thread_vote_author_key',
        null=True,
        on_delete=models.CASCADE)
    vote_type = models.CharField(
        max_length=7,
        blank=False,
        null=False)
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
        db_table = 'thread_vote'
        ordering = ['-date_created']
            
    def __str__(self):
        return 'Thread #{0} {1}d by {2}'.format(
            self.thread.id, self.vote_type, self.user.username)


class PostVote(models.Model):
    '''
    Enables users to like/dislike posts.
    '''
    post = models.ForeignKey(
        Post,
        related_name='post_vote_post_key',
        null=True,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        related_name='post_vote_author_key',
        null=True,
        on_delete=models.CASCADE)
    vote_type = models.CharField(
        max_length=7,
        blank=False,
        null=False)
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
        db_table = 'post_vote'
        
    def __str__(self):
        return 'Post #{0} {1}d by {2}'.format(
            self.post.id, self.vote_type, self.user.username)
