from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse


class ContactViewTests(TestCase):
	def setUp(self):
		self.url = reverse('contact')
		self.valid_payload = {
			'name': 'Test User',
			'email': 'test@example.com',
			'message': 'This is a valid contact message with enough content.',
			'website': '',
		}

	@patch('website.views.send_contact_email_via_mailjet', return_value=True)
	def test_contact_success_when_mailjet_accepts(self, send_contact_email):
		response = self.client.post(self.url, self.valid_payload)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['contact_status'], 'success')
		send_contact_email.assert_called_once()

	@patch('website.views.send_contact_email_via_mailjet')
	def test_contact_honeypot_blocks_without_sending(self, send_contact_email):
		payload = {**self.valid_payload, 'website': 'https://spam.example'}

		response = self.client.post(self.url, payload, HTTP_USER_AGENT='pytest')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['contact_status'], 'blocked')
		send_contact_email.assert_not_called()

	@patch('website.views.send_contact_email_via_mailjet', return_value=False)
	def test_contact_shows_error_when_mailjet_fails(self, send_contact_email):
		response = self.client.post(self.url, self.valid_payload)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['contact_status'], 'error')
		send_contact_email.assert_called_once()
