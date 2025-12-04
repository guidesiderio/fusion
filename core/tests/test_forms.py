from django.test import TestCase
from core.forms import ContactForm


class ContactFormTestCase(TestCase):

    def setUp(self):
        self.name = "John Doe"
        self.email = "john.doe@example.com"
        self.subject = "Inquiry"
        self.message = "I would like to know more about your services."

        self.form_data = {
            "name": self.name,
            "email": self.email,
            "subject": self.subject,
            "message": self.message,
        }

        self.form = ContactForm(data=self.form_data)

    def test_send_email(self):
        form1 = ContactForm(data=self.form_data)
        form1.is_valid()
        res1 = form1.send_email()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_email()

        self.assertEqual(res1, res2)
