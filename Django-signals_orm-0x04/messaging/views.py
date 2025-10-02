from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User

@login_required
def delete_user(request):
    """
    Deletes the currently logged-in user's account.
    Related data will be cleaned up using signals.
    """
    user = request.user
    user.delete()   # This will trigger post_delete signal
    return redirect("/")  # redirect to home or login page
