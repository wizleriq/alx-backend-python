from rest_framework import permissions
from .models import Conversation, Message

class IsParticipnatOfConverstaion(permissions.BasePermission):
    """
    Allow only:
    1. Authenticated users
    2. Participants of a conversation
    3. Participants can only send, view, update, and delete their own messages
    """

def has_permisson(self, request, view):
    return request.user and request.user.is_authenticated

def has_objest_permission(self, request, view, obj):
    if hasattr(obj, 'participants'):
         return request.user in object.participant.all()
    
    if hasattr(obj, 'converstaions'):
        if request.user not in obj.conversation.participant.all()

    
        if request.methodin ['PUT', 'PATCH', 'Delete']:
            return request.user == request.user
        return True
    return False
    
# class IsOwner(permissions.BasePermission):
#     """
#     Custom permission to only allow users to access their own messages/conversations
#     """

#     def has_permission(self, request, view):
#         return request.user and request.user.is_authenticated
    
#     def has_object_permission(self, request, view, obj):
#         """
#         obj can be either a Conversation or a Message.
#         Check if the user is part of the conversation participants.
#         """
#         if isinstance(obj, Conversation):
#             return request.user in obj.participants.all()
        
#         elif isinstance(obj, Message):
#             return request.user in obj.conversation.participants.all()
#         return False
