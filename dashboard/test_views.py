from django.test import TestCase
from django.shortcuts import reverse, render, redirect


class TestViews(TestCase):

    def test_get_dashboard_page(self):
        '''
        Test dashboard page - if redirected to the correct URL and that
        a correct template is used
        '''
        page = self.client.get('/dashboard/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'dashboard.html')
