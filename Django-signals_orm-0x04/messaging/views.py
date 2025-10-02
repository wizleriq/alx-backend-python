from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Message



@login_required
def delete_user(request):
    """
    Deletes the currently logged-in user's account.
    Related data will be cleaned up using signals.
    """
    user = request.user
    user.delete()   # This will trigger post_delete signal
    return redirect("/")  # redirect to home or login page


def conversation_view(request, user_id):
    # Fetch top-level messages with related sender, receiver, and replies
    messages = (
        Message.objects.filter(receiver_id=user_id, parent_message__isnull=True)
        .select_related("sender", "receiver")
        .prefetch_related("replies__sender", "replies__receiver")
        .order_by("timestamp")
    )
    return render(request, "messaging/conversation.html", {"messages": messages})