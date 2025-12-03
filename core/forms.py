from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    subject = forms.CharField(max_length=150, label="Subject")
    message = forms.CharField(widget=forms.Textarea(), label="Your Message")

    def send_email(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        subject = self.cleaned_data["subject"]
        message = self.cleaned_data["message"]

        full_message = f"Message from {name} <{email}>:\n\n{message}"

        email_message = EmailMessage(
            subject=subject,
            body=full_message,
            from_email="contato@fusion.com.br",
            to=[
                "contato@fusion.com.br",
            ],
            headers={"Reply-To": email},
        )
        email_message.send()
