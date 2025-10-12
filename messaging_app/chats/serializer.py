from .models import Conversation, Message
from rest_framework import serializers

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'

class MessageSerializer(serializers. ModelsSerializer):
    class Meta:
        model = Message
        Fields = '__all__'




