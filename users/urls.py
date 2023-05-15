from django.template.defaulttags import url
from django.urls import path
from .views import UserRegisterView, LoginView, ProfilView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfilView.as_view(), name='profile'),
]
