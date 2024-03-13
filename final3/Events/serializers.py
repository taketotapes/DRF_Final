from rest_framework import serializers
from .models import Event, Ticket, Review, Participant
from Notifications.models import Notification
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'is_staff']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['event', 'user', 'registration_date']


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'organizer', 'date', 'location', 'capacity']


class TicketSerializer(serializers.ModelSerializer):
    event_info = EventSerializer(source='event', read_only=True)
    user_info = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'event', 'event_info', 'user', 'user_info']


class ReviewSerializer(serializers.ModelSerializer):
    event_info = EventSerializer(source='event', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

