from django.apps import apps
from django.test import TestCase
from .apps import ForumConfig


class TestForumConfig(TestCase):

    def test_app(self):
        self.assertEqual("forum", ForumConfig.name)
        self.assertEqual("forum", apps.get_app_config("forum").name)
