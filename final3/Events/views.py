from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import generics, status, request
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Event, Ticket, Review
from Notifications.models import Notification
from .serializers import (EventSerializer, TicketSerializer,
                          ReviewSerializer, NotificationSerializer,
                          UserSerializer, ChangePasswordSerializer,
                          ParticipantSerializer)
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .permissions import IsOwnerOrAdmin
from .filters import EventFilter, EventFilterSearch
from rest_framework.response import Response


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserProfileRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"message": "Password updated successfully."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserStatusUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAdminUser]

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = not user.is_active
        user.save()
        return Response({"message": f"User status updated successfully. New status: {'Active' if user.is_active else 'Inactive'}"}, status=status.HTTP_200_OK)


class PromoteToAdminView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_staff = True
        user.save()
        return Response({"message": "User promoted to admin successfully."}, status=status.HTTP_200_OK)


class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_class = EventFilter
    permission_classes = [IsAuthenticated]


class EventDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class EventRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


class TicketListCreate(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]


class ReviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


class NotificationListCreate(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

