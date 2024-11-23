from django.urls import path
from .views import SubmitFeedbackView, FeedbackReportView

urlpatterns = [
    path('submit-feedback/', SubmitFeedbackView.as_view(), name='submit_feedback'),
    path('feedback-report/', FeedbackReportView.as_view(), name='feedback_report'),
]
