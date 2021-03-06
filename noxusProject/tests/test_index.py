from django.test import TestCase
from django.urls import reverse


class IndexPageTest(TestCase) :
    """Testing index page."""
    
    def test_index_page_responsed(self):
        """test the index page could responsed."""

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
