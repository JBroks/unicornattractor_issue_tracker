from django.test import TestCase
from django.shortcuts import reverse, render, redirect
from forum.models import Thread

class TestSearchViews(TestCase):
    
    def test_search_view_page(self):
        '''
        Test search view - if view redirects to the correct
        URL and a correct template is used
        '''
        page = self.client.get("/search_results/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page,'search.html')
    
    def test_search_view_with_query_page(self):
        '''
        Test search view with query - if view redirects to the correct
        URL and a correct template is used
        '''
        page = self.client.get("/search_results/?search=Testing/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page,'search.html')