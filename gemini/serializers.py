from rest_framework import serializers

class GeminiChatbotSerializer(serializers.Serializer):
    prompt = serializers.CharField(
        required=True,
        max_length=500,
        help_text="The user prompt for the chatbot."
    )
