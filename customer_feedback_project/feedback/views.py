from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Feedback

@method_decorator(csrf_exempt, name='dispatch')
class SubmitFeedbackView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            customer_id = data.get("customer_id")
            feedback_text = data.get("feedback_text")

            if not customer_id or not feedback_text:
                return JsonResponse({"message": "Invalid input"}, status=400)
            if len(feedback_text) > 500:
                return JsonResponse({"message": "Feedback too long"}, status=400)

            Feedback.objects.create(customer_id=customer_id, feedback_text=feedback_text)
            return JsonResponse({"message": "Feedback submitted successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"message": f"An error occurred: {str(e)}"}, status=500)


class FeedbackReportView(View):
    def get(self, request):
        try:
            feedbacks = Feedback.objects.all().values("customer_id", "feedback_text", "timestamp")
            feedback_list = list(feedbacks)
            if not feedback_list:
                return JsonResponse({"message": "No feedback available"}, status=404)
            return JsonResponse(feedback_list, safe=False, status=200)
        except Exception as e:
            return JsonResponse({"message": f"An error occurred: {str(e)}"}, status=500)
