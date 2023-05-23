from django.urls import path
from .views import UserRegisterView, LoginView, ProfilView, PasswordChangeView, SendEmailVerificationCodeView, \
    CheckEmailVerificationCodeView, CheckEmailVerificationCodeWithParams


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfilView.as_view(), name='profile'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path("email/verification/", SendEmailVerificationCodeView.as_view(), name="send-email-code"),
    path("email/check-verification/", CheckEmailVerificationCodeView.as_view(), name="check-email-code"),
    path("email/check-verification-code/", CheckEmailVerificationCodeWithParams.as_view(), name="check-email"),
]
