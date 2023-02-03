"""
Teste, ob GET Urls erreichbar sind.
"""
from http import HTTPStatus
from django.test import Client, TestCase
from django.urls import reverse
from events.factories import EventFactory

class EventUrlsTests(TestCase):
    def setUp(self):
        """
        läuft VOR jeder Testmethode
        """
        self.client = Client()
        self.event = EventFactory(name="Hallo Welt!")
    
    def test_event_detail_page_is_public(self):
        """
        Prüfe, ob die Event-Detailseite public ist.
        """
        url = reverse("events:event_detail", kwargs={"pk": self.event.pk})
        response = self.client.get(url)
        self.assertContains(response, text="Hallo Welt!")
        self.assertEqual(response.status_code, HTTPStatus.OK)