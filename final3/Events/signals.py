
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Ticket
from Notifications.models import Notification


@receiver(post_save, sender=Ticket)
def create_notification_on_registration(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        event = instance.event
        message = f"You have successfully registered for the event {event.title}."
        Notification.objects.create(user=user, event=event, message=message)


@receiver(post_delete, sender=Ticket)
def create_notification_on_cancellation(sender, instance, **kwargs):
    user = instance.user
    event = instance.event
    message = f"You have cancelled your registration for the event {event.title}."
    Notification.objects.create(user=user, event=event, message=message)

