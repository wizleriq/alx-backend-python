from django.db import models

# Create your models here.
class Conversation(models.Model):
    participants = models.ManyToManyField('auth.user', related_name= 'converstaions')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Converstaion {self.user}"
    
class Message(models.Model):
    Conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    Sender = models.ForeignKey('auth.user', related_name='sender', on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Message {self.content}"
    

