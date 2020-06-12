from django.test import TestCase
from django.shortcuts import reverse, render, redirect

class TestSearchViews(TestCase):
    
    def test_search_view_page(self):
        '''
        Test search view - if view redirects to the correct
        URL and a correct template is used
        '''
        page = self.client.get("/search_results/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page,'search.html')