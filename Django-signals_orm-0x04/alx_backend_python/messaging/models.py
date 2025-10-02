from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Messae(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.reciever} at {self.timestamp}"
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notofications')
    message = models.ForeignKey, on_delete=models.CASCADE, related_name='notifications'
    is_read = models.BooleanField(default=False)    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification from {self.user} at {self.created_at}"