from django.contrib import admin
from .models import Message, Notification

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'reciever', 'timestamp')
    list_filter = ('sender', 'reciever', 'timestamp')
    search_fields = ('sender_username', 'reciever_username', 'timestamp')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_read', 'created_at')
    list_filter = ("is_read", "created_at")


# Register your models here.

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "message", "text", "is_read", "created_at")
    list_filter = ("is_read", "created_at")