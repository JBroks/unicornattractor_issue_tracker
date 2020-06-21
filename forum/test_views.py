from django.test import TestCase
from django.shortcuts import reverse, render, redirect
from .models import Thread, Post, PostVote, ThreadVote
from django.contrib.auth.models import User
from django.test.client import Client

class TestGetResponses(TestCase):
    
    def setUp(self):
        '''
        Set up a client to be able to login users in order to test views
        using @login_required decorators
        '''
        self.client = Client()
        self.user = User.objects.create_user('joanna',
                                        'joanna@example.com',
                                        'secret')

    def test_get_forum_page(self):
        '''
        Test forum page - if redirected to the correct URL and that
        a correct template is used
        '''
        page = self.client.get("/forum/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "forum.html")
    
    def test_get_view_thread_page(self):
        '''
        Test view thread page - if redirected to the correct URL and that
        a correct template is used
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
         # Create a thread
        thread = Thread(user=self.user,
                        subject="Test Subject",
                        description="Testing description of a thread")
        thread.save()
        page = self.client.get("/forum/view/thread/{0}/".format(thread.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "view_thread.html")
    
    def test_get_add_thread_page(self):
        '''
        Test add thread page - if redirected to the correct URL and that
        a correct template is used
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        # Test page
        page = self.client.get("/forum/new/thread/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_thread.html")
    
    def test_get_edit_thread_page(self):
        # Login user
        self.client.login(username='joanna', password='secret')
        # Create a thread
        thread = Thread(user=self.user,
                        subject="Test Subject",
                        description="Testing description of a thread")
        thread.save()

        page = self.client.get("/forum/edit/thread/{0}/".format(thread.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_thread.html")

class TestDeleteViews(TestCase):
    
    def setUp(self):
        '''
        Set up a client to be able to login users in order to test views
        using @login_required decorators
        '''
        self.client = Client()
        self.user = User.objects.create_user('joanna',
                                        'joanna@example.com',
                                        'secret')
                                        
    def test_get_delete_thread_by_author_page(self):
        '''
        Test case where thread author deletes their own thread
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        # Create a thread
        thread = Thread(user=self.user,
                        subject="Test Subject",
                        description="Testing description of a thread")
        thread.save()
        
        # Test redirect when thread is deleted
        page = self.client.get("/forum/delete/thread/{0}/".format(thread.id))
        self.assertEqual(page.status_code, 302)
    
    def test_get_delete_thread_by_other_user_page(self):
        '''
        Test case when user attempts to delete a thread created by other user
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        
        other_user = User.objects.create_user('john',
                                        'john@example.com',
                                        'secret2')
       # Create a thread
        thread = Thread(user=other_user,
                        subject="Test Subject",
                        description="Testing description of a thread")
        thread.save()
        
        # Test redirect when thread is deleted
        page = self.client.get("/forum/delete/thread/{0}/".format(thread.id))
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('view_thread', kwargs={'pk':1}))
        
    def test_get_delete_post_by_author_page(self):
        '''
        Test case where post author deletes their own post
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        
        # Create a thread
        thread = Thread(user=self.user,
                        subject="Test Subject",
                        description="Testing description of a thread")
        thread.save()
        
        # Create a post
        post = Post(user=self.user,
                    thread=thread,
                    post="Testing post description")
        post.save()
        
        # Test redirect when comment is deleted
        page = self.client.get(
            "/forum/view/thread/{0}/posts/delete/post/{1}".format(
                thread.id, post.id), follow=True)
        self.assertEqual(page.status_code, 200)
    
        
    def test_get_delete_post_by_other_user_page(self):
        '''
        Test case where a user tries to delete someone else's post
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        # Create other user
        other_user = User.objects.create_user('john',
                                        'john@example.com',
                                        'secret2')
        # Create a thread
        thread = Thread(user=self.user,
                        subject="Test Subject",
                        description="Testing description of a thread")
        thread.save()
        
        # Create a post
        post = Post(user=other_user,
                    thread=thread,
                    post="Testing post description")
        post.save()
        
        # Test redirect when comment is deleted
        page = self.client.get(
            "/forum/view/thread/{0}/posts/delete/post/{1}".format(
                thread.id, post.id), follow=True)
        self.assertEqual(page.status_code, 200)
        
        # Test error message
        messages = list(page.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),"Error! You don't have a permission to \
                        delete this post.")
    
class TestThreadVoting(TestCase):
    
    def setUp(self):
        '''
        Set up a client to be able to login users in order to test views
        using @login_required decorators
        '''
        self.client = Client()
        self.user = User.objects.create_user('joanna',
                                        'joanna@example.com',
                                        'secret')  
   
    def test_get_vote_thread_page(self):
        '''
        Test that checks if page reverses to view thread page after
        the thread is liked/disliked
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        # Create a thread
        thread = Thread(subject="Test Subject",
                        description="Testing description of a thread")
        thread.save()

        # Test redirect when thread is voted
        page = self.client.get("/forum/view/thread/{0}/vote/{1}/".format(thread.id, "like"))
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('view_thread', kwargs={'pk':1}))
                                        
    def test_thread_cast_the_same_vote_twice(self):
        '''
        Test that checks if vote is removed when user votes again
        the same way as before
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        # Create a thread
        thread = Thread(subject="Test Subject",
                        description="Testing description of a thread")
        thread.save()
        
        # Create a vote
        vote = ThreadVote(thread=thread,
                        vote_type="like",
                        user=self.user)
        vote.save()
        
        # Count votes
        initial_count = ThreadVote.objects.all().count()
        self.assertEqual(initial_count, 1)
        
        # Test redirect when thread is liked/disliked
        page = self.client.get("/forum/view/thread/{0}/vote/{1}/".format(thread.id,"like"))
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('view_thread', kwargs={'pk':1}))
        
        # Final count
        final_count = ThreadVote.objects.all().count()
        self.assertEqual(final_count, 0)
    
    def test_thread_change_vote_from_like_to_dislike(self):
        '''
        Test that thread liked initialy is changing to dislike when user votes 
        again for the same thread
        Check if user gets only one vote per thread and the final vote is 
        'dislike' as per their last choice
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        # Create a thread
        thread = Thread(subject="Test Subject",
                        description="Testing description of a thread")
        thread.save()
        
        # Create a vote
        vote = ThreadVote(thread=thread,
                        vote_type="like",
                        user=self.user)
        vote.save()
        
        # Count votes
        initial_count = ThreadVote.objects.all().count()
        self.assertEqual(initial_count, 1)
        
        # Test redirect when thread is voted & dislike the thread
        page = self.client.get("/forum/view/thread/{0}/vote/{1}/".format(thread.id,"dislike"))
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('view_thread', kwargs={'pk':1}))
        
        # Final count
        final_count = ThreadVote.objects.all().count()
        self.assertEqual(final_count, 1)
        
        # Test vote type
        final_vote = ThreadVote.objects.get(user=self.user)
        self.assertEqual(final_vote.vote_type, "dislike")
    
    def test_thread_change_vote_from_dislike_to_like(self):
        '''
        Test that thread disliked initialy is changing to 'like' when user votes 
        again for the same thread
        Check if user gets only one vote per thread and the final vote is 
        'like' as per their last choice
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        # Create a thread
        thread = Thread(subject="Test Subject",
                        description="Testing description of a thread")
        thread.save()
        
        # Create a vote
        vote = ThreadVote(thread=thread,
                        vote_type="dislike",
                        user=self.user)
        vote.save()
        
        # Count votes
        initial_count = ThreadVote.objects.all().count()
        self.assertEqual(initial_count, 1)
        
        # Test redirect when thread is voted & dislike the thread
        page = self.client.get("/forum/view/thread/{0}/vote/{1}/".format(thread.id,"like"))
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('view_thread', kwargs={'pk':1}))
        
        # Final count
        final_count = ThreadVote.objects.all().count()
        self.assertEqual(final_count, 1)
        
        # Test vote type
        final_vote = ThreadVote.objects.get(user=self.user)
        self.assertEqual(final_vote.vote_type, "like")
        
class TestPostVoting(TestCase):
    
    def setUp(self):
        '''
        Set up a client to be able to login users in order to test views
        using @login_required decorators
        '''
        self.client = Client()
        self.user = User.objects.create_user('joanna',
                                        'joanna@example.com',
                                        'secret')  
    
    def test_get_vote_post_page(self):
        '''
        Test that checks if page reverses to view thread page after
        the post is liked/disliked
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        # Create a thread
        thread = Thread(subject="Test Subject",
                        description="Testing description of a thread")
        thread.save()
        # Create a post
        post = Post(user=self.user,
                    thread=thread,
                    post="Testing post description")
        post.save()
        # Test redirect when thread is voted
        page = self.client.get("/forum/view/thread/{0}/posts/vote/{1}/{2}/".format(thread.id,post.id,"dislike"))
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('view_thread', kwargs={'pk':1}))
        
    def test_post_cast_the_same_vote_twice(self):
        '''
        Test that checks if vote is removed when user votes again
        the same way as before
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        # Create a thread
        thread = Thread(subject="Test Subject",
                        description="Testing description of a thread")
        thread.save()
        # Create a post
        post = Post(user=self.user,
                    thread=thread,
                    post="Testing post description")
        post.save()
        # Create a vote
        vote = PostVote(post=post,
                        vote_type="like",
                        user=self.user)
        vote.save()
        
        # Count votes
        initial_count = PostVote.objects.all().count()
        self.assertEqual(initial_count, 1)
        
        # Test redirect when post is voted
        page = self.client.get("/forum/view/thread/{0}/posts/vote/{1}/{2}/".format(thread.id,post.id,"like"))
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('view_thread', kwargs={'pk':1}))
        
        # Final count
        final_count = PostVote.objects.all().count()
        self.assertEqual(final_count, 0)
        
    def test_post_change_vote_from_like_to_dislike(self):
        '''
        Test that post liked initialy is changing to dislike when user votes 
        again for the same post
        Check if user gets only one vote per post and the final vote is 
        'dislike' as per their last choice
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        # Create a thread
        thread = Thread(subject="Test Subject",
                        description="Testing description of a thread")
        thread.save()
         # Create a post
        post = Post(user=self.user,
                    thread=thread,
                    post="Testing post description")
        post.save()
        # Create a vote
        vote = PostVote(post=post,
                        vote_type="like",
                        user=self.user)
        vote.save()
        
        # Count votes
        initial_count = PostVote.objects.all().count()
        self.assertEqual(initial_count, 1)
        
        # Test redirect when post is voted & change vote to 'dislike'
        page = self.client.get("/forum/view/thread/{0}/posts/vote/{1}/{2}/".format(thread.id,post.id,"dislike"))
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('view_thread', kwargs={'pk':1}))
        
        # Final count
        final_count = PostVote.objects.all().count()
        self.assertEqual(final_count, 1)
        
        # Test vote type
        final_vote = PostVote.objects.get(user=self.user)
        self.assertEqual(final_vote.vote_type, "dislike")
    
    def test_post_change_vote_from_dislike_to_like(self):
        '''
        Test that post disliked initialy is changing to like when user votes 
        again for the same post
        Check if user gets only one vote per post and the final vote is 
        'like' as per their last choice
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        # Create a thread
        thread = Thread(subject="Test Subject",
                        description="Testing description of a thread")
        thread.save()
         # Create a post
        post = Post(user=self.user,
                    thread=thread,
                    post="Testing post description")
        post.save()
        # Create a vote
        vote = PostVote(post=post,
                        vote_type="dislike",
                        user=self.user)
        vote.save()
        
        # Count votes
        initial_count = PostVote.objects.all().count()
        self.assertEqual(initial_count, 1)
        
        # Test redirect when post is voted & change vote to 'like'
        page = self.client.get("/forum/view/thread/{0}/posts/vote/{1}/{2}/".format(thread.id,post.id,"like"))
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('view_thread', kwargs={'pk':1}))
        
        # Final count
        final_count = PostVote.objects.all().count()
        self.assertEqual(final_count, 1)
        
        # Test vote type
        final_vote = PostVote.objects.get(user=self.user)
        self.assertEqual(final_vote.vote_type, "like")