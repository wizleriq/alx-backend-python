from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory

@receiver(pre_save, sender=Message)
def login_message_edit(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:
                MessageHistory.objects.create(
                    mesage=old_message,
                    old_content=old_message.content,
                    new_content=instance.content,
                )

                instance.edited = True
        except Message.DoesNotExist:
            pass
                


@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance,
            text=f"You have a new message from {instance.sender.username}"
        )
