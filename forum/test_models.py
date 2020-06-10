from django.test import TestCase
from .models import Thread, Post
from django.contrib.auth.models import User
import datetime

# Create your tests here.
class TestThread(TestCase):
        
        def test_thread_creation(self):
            """
            Test that when created a thread a correct text is displayed
            """
            # Create a new user
            new_user = User.objects.create_user({
                                'username': 'joanna', 
                                'email': 'joanna@example.com',
                                'password': 'secret'
                                })
            # Create a new thread                    
            new_thread = Thread.objects.create(user=new_user,
                                subject="Test Subject",
                                description="Testing description of a thread")
            # Retrive the thread
            thread = Thread.objects.get(id=1)
            displayed_object_name = f"Forum thread #{new_thread.id} [{new_thread.subject}] added by {new_user.username}"
            self.assertEquals(displayed_object_name, str(thread))
    
        def test_thread_post_summary_info(self):
            '''
            Test latest post date, latest post author, and post count bound 
            methods added to Thread model
            '''
            # Create a new user
            new_user = User.objects.create_user({
                                'username': 'joanna', 
                                'email': 'joanna@example.com',
                                'password': 'secret'
                                })
            second_user = User.objects.create_user({
                                'username': 'suzanne', 
                                'email': 'suzanne@example.com',
                                'password': 'secret2'
                                })
            # Create a new thread                    
            new_thread = Thread.objects.create(user=new_user,
                                subject="Test Subject",
                                description="Testing description of a thread")
             # Create a new post                    
            new_post = Post.objects.create(user=new_user,
                                thread=new_thread,
                                post="Test Post Text",
                                date_updated=datetime.date.today() - datetime.timedelta(days=1)
                                )
            second_post = Post.objects.create(user=new_user,
                                thread=new_thread,
                                post="Test Post Text2",
                                date_updated=datetime.date.today()
                                )
            
            # Test latest post date method
            post = Post.objects.get(id=2)
            expected_latest_post_date = new_thread.latest_post_date()
            self.assertEquals(expected_latest_post_date, post.date_updated)
            
            # Test latest author method
            post = Post.objects.get(id=2)
            expected_latest_post_author = new_thread.latest_post_author()
            self.assertEquals(expected_latest_post_author, post.user)
            
            # Test post count
            expected_post_count = new_thread.post_count()
            self.assertEquals(expected_post_count, 2)
            