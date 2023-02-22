from django.urls import path
from .views import *
urlpatterns = [
    path('api/user/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/user/login/', LoginView.as_view(), name='login'),
    path('api/user/logout/', LogoutView.as_view(), name='logout'),
]
