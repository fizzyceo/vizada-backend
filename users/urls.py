# users/urls.py
from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('jwt/user/', CustomTokenCreateView.as_view(), name='jwt-create'),
    path('user-info/<str:access_token>/', UserFromTokenView.as_view(), name='user-info'),
    path('api/updateprofile/', UpdateUserView.as_view(), name='update-profile'),
    path('auth/logout/', LogoutView.as_view(), name="logout"),
    path('api/getusers/', views.UserListView.as_view(), name='user-list'),
    path('api/sendcontactusemail/', SendAcontactusEmailView.as_view(), name='send-admin-email'),
]
