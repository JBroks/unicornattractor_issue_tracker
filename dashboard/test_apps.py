from django.apps import apps
from django.test import TestCase
from .apps import DashboardConfig


class TestDashboardConfig(TestCase):
    '''
    Test application name configuration.
    '''
    def test_app(self):
        self.assertEqual("dashboard", DashboardConfig.name)
        self.assertEqual("dashboard", apps.get_app_config("dashboard").name)
