from django.test import TestCase
from django.urls import reverse
from .models import Feedback
class FeedbackTestCase(TestCase):
    def setUp(self):
        Feedback.objects.create(customer_id=1, feedback_text="Great service!")

    def test_submit_feedback_valid(self):
        response = self.client.post(
            reverse('submit_feedback'),
            data={"customer_id": 2, "feedback_text": "Excellent!"}, 
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

    def test_submit_feedback_invalid(self):
        response = self.client.post(
            reverse('submit_feedback'),
            data={"customer_id": None, "feedback_text": "Great!"}, 
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)

    def test_feedback_report(self):
        response = self.client.get(reverse('feedback_report'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
