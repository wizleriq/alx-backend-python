from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsParticipantOfConversation
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

def get_queryset(self):
        # Allow filtering by conversation_id
        conversation_id = self.request.query_params.get("conversation_id")
        if conversation_id:
            return Message.objects.filter(conversation_id=conversation_id)
        return Message.objects.all()

    def perform_create(self, serializer):
        conversation_id = self.request.data.get("conversation_id")
        conversation = Conversation.objects.filter(id=conversation_id).first()

        # Ensure the user is part of the conversation
        if not conversation or self.request.user not in conversation.participants.all():
            return Response(
                {"detail": "You are not allowed to send a message in this conversation."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Save the message with sender and conversation
        serializer.save(sender=self.request.user, conversation=conversation)
# class ConversationViewSet(viewsets.ModelViewSet):
#     queryset = Conversation.objects.all()
#     serializer_class = ConversationSerializer
#     permission_classes = [IsAuthenticated, IsParticipantOfConversation]


# class MessageViewSet(viewsets.ModelViewSet):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     permission_classes = [IsAuthenticated, IsParticipantOfConversation]
