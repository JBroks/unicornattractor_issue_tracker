from django.test import TestCase
from .models import Ticket, Upvote, Donation, Comment
from django.contrib.auth.models import User
import datetime

# Create your tests here.
class TestTicket(TestCase):
        
        def test_ticket_creation(self):
            """
            Test that when created a ticket a correct text is displayed
            """
            # Create a new user
            new_user = User.objects.create_user({
                                'username': 'joanna', 
                                'email': 'joanna@example.com',
                                'password': 'secret'
                                })
            # Create a new ticket                    
            new_ticket = Ticket.objects.create(user=new_user,
                                subject="Test Subject",
                                ticket_type="Bug",
                                ticket_status="Open",
                                description="Testing description of a ticket")
            # Retrive the ticket
            ticket = Ticket.objects.get(id=1)
            displayed_object_name = f"Ticket #{new_ticket.id} [{new_ticket.ticket_status}] {new_ticket.ticket_type} - {new_ticket.subject}"
            self.assertEquals(displayed_object_name, str(ticket))

class TestUpvote(TestCase):
    
        def test_upvote_creation(self):
            """
            Test that when created an upvote a correct text is displayed
            """
            # Create a new user
            new_user = User.objects.create_user({
                                'username': 'joanna', 
                                'email': 'joanna@example.com',
                                'password': 'secret'
                                })
            # Create a new ticket                    
            new_ticket = Ticket.objects.create(user=new_user,
                                subject="Test Subject",
                                ticket_type="Bug",
                                ticket_status="Open",
                                description="Testing description of a ticket")
            # Create an upvote
            new_upvote = Upvote.objects.create(user=new_user,
                                            ticket=new_ticket)
            # Retrive the upvote
            upvote = Upvote.objects.get(id=1)
            displayed_object_name = f"Ticket #{new_upvote.ticket.id} upvoted by {new_upvote.user.username}"
            self.assertEquals(displayed_object_name, str(upvote))
            
class TestDonation(TestCase):
    
        def test_donation_creation(self):
            """
            Test that when created a donation a correct text is displayed
            """
            # Create a new user
            new_user = User.objects.create_user({
                                'username': 'joanna', 
                                'email': 'joanna@example.com',
                                'password': 'secret'
                                })
            # Create a new ticket                    
            new_ticket = Ticket.objects.create(user=new_user,
                                subject="Test Subject",
                                ticket_type="Bug",
                                ticket_status="Open",
                                description="Testing description of a ticket")
            # Create a donation
            new_donation = Donation.objects.create(user=new_user,
                                            ticket=new_ticket,
                                            donation_amount="5")
            # Retrive the donation
            donation = Donation.objects.get(id=1)
            displayed_object_name = f"€{new_donation.donation_amount} donated by {new_donation.user.username} for ticket #{new_donation.ticket.id}"
            self.assertEquals(displayed_object_name, str(donation))
            
class TestComment(TestCase):
    
        def test_comment_creation(self):
            """
            Test that when created a comment a correct text is displayed
            """
            # Create a new user
            new_user = User.objects.create_user({
                                'username': 'joanna', 
                                'email': 'joanna@example.com',
                                'password': 'secret'
                                })
            # Create a new ticket                    
            new_ticket = Ticket.objects.create(user=new_user,
                                subject="Test Subject",
                                ticket_type="Bug",
                                ticket_status="Open",
                                description="Testing description of a ticket")
            # Create a comment
            new_comment = Comment.objects.create(user=new_user,
                                            ticket=new_ticket,
                                            comment="Testing comment text")
            # Retrive the comment
            comment = Comment.objects.get(id=1)
            displayed_object_name = f"Comment #{new_comment.id} added by {new_comment.user.username} for ticket #{new_comment.ticket.id}"
            self.assertEquals(displayed_object_name, str(comment))