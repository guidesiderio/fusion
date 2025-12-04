from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.form_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "subject": "Inquiry",
            "message": "I would like to know more about your services.",
        }

        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy("index"), data=self.form_data)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        invalid_data = self.form_data.copy()
        invalid_data["email"] = "invalid-email-format"

        request = self.client.post(reverse_lazy("index"), data=invalid_data)
        self.assertEqual(request.status_code, 200)
