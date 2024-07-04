from django.test import TestCase
from unittest.mock import patch

from core.services.email_service import EmailService


class EmailServiceTestCase(TestCase):

    def setUp(self):
        self.service_class = EmailService

    @patch('core.services.email_service.send_mail')
    def test_send_email_with_default_from(self, mocked_send_mail):
        mocked_send_mail.return_value = 1
        service = EmailService()
        subject = 'Test email'
        message = 'This is a test email'
        recipient_list = ['email1', 'email2']
        service.send_email(
            subject=subject,
            message=message,
            recipient_list=recipient_list
        )
        mocked_send_mail.assert_called_once_with(
            subject,
            message,
            None,
            recipient_list,
            fail_silently=False,
        )
