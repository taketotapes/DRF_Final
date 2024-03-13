"""
URL configuration for final3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from final3 import settings
from rest_framework_simplejwt.views import (
     TokenObtainPairView,
     TokenRefreshView,
)

from Events.views import (EventListCreate, EventRetrieveUpdateDestroy, TicketListCreate, TicketRetrieveUpdateDestroy,
                          ReviewListCreate,
                          ReviewRetrieveUpdateDestroy, NotificationListCreate, NotificationRetrieveUpdateDestroy,
                          UserCreate, ChangePasswordView, UserProfileRetrieveUpdate, UserStatusUpdate,
                          PromoteToAdminView,
                          EventList, )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/register/', UserCreate.as_view(), name='user-create'),
    path('users/profile/', UserProfileRetrieveUpdate.as_view(), name='user-profile'),
    path('users/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('users/<int:pk>/update-status/', UserStatusUpdate.as_view(), name='update-user-status'),
    path('users/<int:pk>/promote-to-admin/', PromoteToAdminView.as_view(), name='promote-to-admin'),

    path('events/', EventListCreate.as_view(), name='event-list-create'),
    path('events/list/', EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroy.as_view(), name='event-retrieve-update-destroy'),

    path('tickets/', TicketListCreate.as_view(), name='ticket-list-create'),
    path('tickets/<int:pk>/', TicketRetrieveUpdateDestroy.as_view(), name='ticket-retrieve-update-destroy'),

    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroy.as_view(), name='review-retrieve-update-destroy'),

    path('notifications/', NotificationListCreate.as_view(), name='notification-list-create'),
    path('notifications/<int:pk>/', NotificationRetrieveUpdateDestroy.as_view(),
         name='notification-retrieve-update-destroy'),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
