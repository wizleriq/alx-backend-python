from rest_framework import permissions
from .models import Conversation, Message

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow users to access their own messages/conversations
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        """
        obj can be either a Conversation or a Message.
        Check if the user is part of the conversation participants.
        """
        if isinstance(obj, Conversation):
            return request.user in obj.participants.all()
        elif isinstance(obj, Message):
            return request.user in obj.conversation.participants.all()
        return False
