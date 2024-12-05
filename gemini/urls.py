from django.urls import path
from .views import GeminiChatbotView

urlpatterns = [
    path('gemini-chat/', GeminiChatbotView.as_view(), name='gemini-chat'),
]
