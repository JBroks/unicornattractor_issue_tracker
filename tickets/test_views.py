from django.test import TestCase
from django.shortcuts import reverse, render, redirect
from .models import Ticket, Upvote, Donation, Comment
from django.contrib.auth.models import User
from django.test.client import Client


class TestViews(TestCase):
    
    def setUp(self):
        '''
        Set up a client to be able to login users in order to test views
        using @login_required decorators.
        '''
        self.client = Client()
        self.user = User.objects.create_user('joanna',
                                             'joanna@example.com',
                                             'secret')

    def test_get_all_tickets_page(self):
        '''
        Test all tickets page - if redirected to the correct URL and that
        a correct template is used
        '''
        page = self.client.get('/tickets/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'all_tickets.html')
        
    def test_get_all_tickets_with_filters_page(self):
        '''
        Test all tickets page with filters - if redirected to the correct
        URL and that a correct template is used.
        '''
        page = self.client.get(
            '/tickets/?ticket-type=Feature&ticket-status=Open/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'all_tickets.html')
        
        page = self.client.get('/tickets/?ticket-type=Feature/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'all_tickets.html')
        
        page = self.client.get('/tickets/?ticket-status=Open/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'all_tickets.html')
        
    def test_get_add_ticket_page(self):
        '''
        Test add ticket page - if redirected to the correct URL and that
        a correct template is used.
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        
        page = self.client.get('/tickets/new/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'add_ticket.html')
    
    def test_get_edit_ticket_page(self):
        '''
        Test edit ticket page - if redirected to the correct URL and that
        a correct template is used.
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        
        # Create a ticket
        ticket = Ticket(subject='Test Subject',
                        ticket_type='Bug',
                        ticket_status='Open',
                        description='Testing description of a ticket')
        ticket.save()

        page = self.client.get('/tickets/edit/ticket/{0}/'.format(ticket.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'add_ticket.html')
    
    def test_get_upvote_ticket_without_donation_page(self):
        '''
        Test that checks if page reverses to view ticket page after
        the ticket is upvoted.
        Ticket type bug does not require donation.
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        
        # Create a ticket
        ticket = Ticket(subject='Test Subject',
                        ticket_type='Bug',
                        ticket_status='Open',
                        description='Testing description of a ticket')
        ticket.save()
        
        page = self.client.get('/tickets/upvote/ticket/{0}/'.format(ticket.id))
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('view_ticket', kwargs={'pk': 1}))
    
    def test_get_downvote_ticket_page(self):
        '''
        Test that checks if redirects to the correct url after
        the ticket is downvoted.
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        
        # Create a ticket
        ticket = Ticket(user=self.user,
                        subject='Test Subject',
                        ticket_type='Bug',
                        ticket_status='Open',
                        description='Testing description of a ticket')
        ticket.save()
        
        # Create upvote so it exist before you test downvote url
        upvote = Upvote(ticket=ticket,
                        user=self.user)
        upvote.save()
        
        page = self.client.get(
            '/tickets/downvote/ticket/{0}/'.format(ticket.id))
        self.assertEqual(page.status_code, 302)
     
    def test_get_delete_ticket_by_author_page(self):
        '''
        Test case where ticket author deletes their own ticket.
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        
        # Create a ticket
        ticket = Ticket(user=self.user,
                        subject='Test Subject',
                        ticket_type='Bug',
                        ticket_status='Open',
                        description='Testing description of a ticket')
        ticket.save()
        
        page = self.client.get('/tickets/delete/ticket/{0}/'.format(ticket.id))
        self.assertEqual(page.status_code, 302)
    
    def test_get_delete_ticket_by_other_user_page(self):
        '''
        Test case when user attempts to delete a ticket created by other user.
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        
        # Create other user that will be an author of the ticket
        other_user = User.objects.create_user('john',
                                              'john@example.com',
                                              'secret2')

        # Create a ticket
        ticket = Ticket(user=other_user,
                        subject='Test Subject',
                        ticket_type='Bug',
                        ticket_status='Open',
                        description='Testing description of a ticket')
        ticket.save()
        
        page = self.client.get('/tickets/delete/ticket/{0}/'.format(ticket.id))
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('view_ticket', kwargs={'pk': 1}))
        
    def test_404_error_if_comment_does_not_exist(self):
        '''
        Test if error will come up if attempted to edit comment that
        does not exist.
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        
        # Create a ticket
        ticket = Ticket(user=self.user,
                        subject='Test Subject',
                        ticket_type='Bug',
                        ticket_status='Open',
                        description='Testing description of a ticket')
        ticket.save()
        
        page = self.client.get(
            '/tickets/view/ticket/{0}/comments/edit/comment/{1}'.format(
                ticket.id, None))
        self.assertEqual(page.status_code, 404)
    
    def test_get_delete_comment_by_author_page(self):
        '''
        Test case where comment author deletes their own comment.
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        
        # Create a ticket
        ticket = Ticket(user=self.user,
                        subject='Test Subject',
                        ticket_type='Bug',
                        ticket_status='Open',
                        description='Testing description of a ticket')
        ticket.save()
        
        # Create a comment
        comment = Comment(user=self.user,
                          ticket=ticket,
                          comment='Testing comment description')
        comment.save()
        
        page = self.client.get(
            '/tickets/view/ticket/{0}/comments/delete/comment/{1}'.format(
                ticket.id, comment.id), follow=True)
        self.assertEqual(page.status_code, 200)
    
    def test_get_delete_comment_by_other_user_page(self):
        '''
        Test case where a user tries to delete someone else's comment.
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        
        # Create other user that will be an author of the comment
        other_user = User.objects.create_user('john',
                                              'john@example.com',
                                              'secret2')
        
        # Create a ticket
        ticket = Ticket(user=self.user,
                        subject='Test Subject',
                        ticket_type='Bug',
                        ticket_status='Open',
                        description='Testing description of a ticket')
        ticket.save()
        
        # Create a comment
        comment = Comment(user=other_user,
                          ticket=ticket,
                          comment='Testing comment description')
        comment.save()
        
        # Test redirect when comment is deleted
        page = self.client.get(
            '/tickets/view/ticket/{0}/comments/delete/comment/{1}'.format(
                ticket.id, comment.id), follow=True)
        self.assertEqual(page.status_code, 200)
        
        # Test error message
        messages = list(page.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Error! You don't have a"
                         " permission to delete this comment.")
