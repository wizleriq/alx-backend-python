from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from django.db.models.signals import post_delete
from django.contrib.auth.models import User

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


@receiver(post_delete, sender=User)
def cleanup_user_related_data(sender, instance, **kwargs):
    """
    When a user is deleted, remove all related messages, notifications,
    and message histories.
    """
    # Delete all messages sent or received by this user
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    # Delete all notifications for this user
    Notification.objects.filter(user=instance).delete()

    # Delete all message histories linked to the user's messages
    MessageHistory.objects.filter(message__sender=instance).delete()
    MessageHistory.objects.filter(message__receiver=instance).delete()
