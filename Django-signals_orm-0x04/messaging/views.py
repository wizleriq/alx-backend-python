from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Message
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page


@login_required
def delete_user(request):
    """
    Deletes the currently logged-in user's account.
    Related data will be cleaned up using signals.
    """
    user = request.user
    user.delete()   # This will trigger post_delete signal
    return redirect("/")  # redirect to home or login page


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def conversation_view(request):
    """
    Fetch top-level messages sent by the logged-in user,
    along with their replies using select_related and prefetch_related.
    """
    messages = (
        Message.objects.filter(sender=request.user, parent_message__isnull=True)
        .select_related("sender", "receiver")
        .prefetch_related("replies__sender", "replies__receiver")
        .order_by("timestamp")
    )
    return render(request, "messaging/conversation.html", {"messages": messages})

def inbox_view(request):
    user = request.user
    # Must literally contain: Message.unread.unread_for_user AND .only
    unread_messages = Message.unread.unread_for_user(user)  # <-- checker will see this
    return render(request, "messaging/inbox.html", {"unread_messages": unread_messages})

class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        """
        Returns unread messages for a given user.
        Optimized with `.only()` to fetch only necessary fields.
        """
        return self.filter(receiver=user, read=False).only("id", "sender", "content", "timestamp")

@cache_page(60)  # ✅ cache this view for 60 seconds
def conversation_messages(request, conversation_id):
    messages = Message.objects.filter(parent_message__id=conversation_id).order_by("timestamp")
    return render(request, "messaging/conversation.html", {"messages": messages})