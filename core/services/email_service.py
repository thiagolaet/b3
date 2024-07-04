from django.core.mail import send_mail
from django.conf import settings


class EmailService:

    def __init__(self, from_email=None):
        self.from_email = from_email

    def send_email(self, subject, message, recipient_list):
        return send_mail(
            subject,
            message,
            self.from_email,
            recipient_list,
            fail_silently=False,
        )
