from django.test import TestCase
from .models import Thread, Post, ThreadVote, PostVote
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
    
        def test_thread_latest_post_and_count_methods(self):
            '''
            Test latest post date, latest post author, and post count bound 
            methods added to the Thread model
            '''
            # Create two users
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
             # Create two post                    
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
            
        def test_thread_votes_count_method(self):
            '''
            Test count likes & count dislikes bound methods 
            added to the Thread model
            '''
             # Create two users
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
            # Create two threads                    
            new_thread = Thread.objects.create(user=new_user,
                                subject="Test Subject",
                                description="Testing description of a thread")
            second_thread = Thread.objects.create(user=second_user,
                                subject="Test Subject2",
                                description="Testing description of a thread2")
            # Create thread votes                    
            thread_vote_1 = ThreadVote.objects.create(user=new_user,
                                thread=new_thread,
                                vote_type="like")
            thread_vote_2 = ThreadVote.objects.create(user=new_user,
                                thread=second_thread,
                                vote_type="dislike")
            thread_vote_3 = ThreadVote.objects.create(user=second_user,
                                thread=new_thread,
                                vote_type="like")
            
            # Test likes count
            expected_likes_count_new_thread = new_thread.thread_likes_count()
            self.assertEquals(expected_likes_count_new_thread, 2)
            expected_likes_count_second_thread = second_thread.thread_likes_count()
            self.assertEquals(expected_likes_count_second_thread, 0)
            
            # Test dislikes count
            expected_dislikes_count_new_thread = new_thread.thread_dislikes_count()
            self.assertEquals(expected_dislikes_count_new_thread, 0)
            expected_dislikes_count_second_thread = second_thread.thread_dislikes_count()
            self.assertEquals(expected_dislikes_count_second_thread, 1)
        
       
        def test_post_creation(self):
            """
            Test that when created a post a correct text is displayed
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
            # Create a new post                    
            new_post = Post.objects.create(user=new_user,
                                thread=new_thread,
                                post="Testing description of a post")
            # Retrive the post
            post = Post.objects.get(id=1)
            displayed_object_name = f"Post #{new_post.id} added by {new_user.username} for thread #{new_thread.id}"
            self.assertEquals(displayed_object_name, str(post))
        
        def test_post_votes_method(self):
            '''
            Test count likes, count dislikes, and post voters bound methods 
            added to the Post model
            '''
             # Create two users
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
            # Create posts
            new_post = Post.objects.create(user=new_user,
                                thread=new_thread,
                                post="Testing description of a post")
            second_post = Post.objects.create(user=new_user,
                                thread=new_thread,
                                post="Testing description of a post2")
            # Create post votes                    
            post_vote_1 = PostVote.objects.create(user=new_user,
                                post=new_post,
                                vote_type="like")
            post_vote_2 = PostVote.objects.create(user=new_user,
                                post=second_post,
                                vote_type="dislike")
            post_vote_3 = PostVote.objects.create(user=second_user,
                                post=new_post,
                                vote_type="like")
            
            # Test likes count
            expected_likes_count_new_post = new_post.post_likes_count()
            self.assertEquals(expected_likes_count_new_post, 2)
            expected_likes_count_second_post = second_post.post_likes_count()
            self.assertEquals(expected_likes_count_second_post, 0)
            
            # Test dislikes count
            expected_dislikes_count_new_post = new_post.post_dislikes_count()
            self.assertEquals(expected_dislikes_count_new_post, 0)
            expected_dislikes_count_second_post = second_post.post_dislikes_count()
            self.assertEquals(expected_dislikes_count_second_post, 1)
            
            # Post voters list
            expected_post_voters_new_post = new_post.post_voters().count()
            self.assertEquals(expected_post_voters_new_post, 2)
        
        def test_thread_vote_creation(self):
            """
            Test that when created a thread vote a correct text is displayed
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
            # Create a new thread vote                    
            thread_vote = ThreadVote.objects.create(user=new_user,
                                thread=new_thread,
                                vote_type="like")
            # Retrive the vote
            vote = ThreadVote.objects.get(id=1)
            displayed_object_name = f"Thread #{vote.thread.id} {vote.vote_type}d by {vote.user.username}"
            self.assertEquals(displayed_object_name, str(vote))
        
        def test_post_vote_creation(self):
            """
            Test that when created a post vote a correct text is displayed
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
            # Create posts
            new_post = Post.objects.create(user=new_user,
                                thread=new_thread,
                                post="Testing description of a post")
            # Create a new post vote                  
            post_vote = PostVote.objects.create(user=new_user,
                                post=new_post,
                                vote_type="like")
            # Retrive the vote
            vote = PostVote.objects.get(id=1)
            displayed_object_name = f"Post #{vote.post.id} {vote.vote_type}d by {vote.user.username}"
            self.assertEquals(displayed_object_name, str(vote))