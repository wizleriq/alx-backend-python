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
    unread_message = Message.unread.fo-user(user)
    return render(request, "messaging/inbox.html", {"unread_messages": unread_messages})