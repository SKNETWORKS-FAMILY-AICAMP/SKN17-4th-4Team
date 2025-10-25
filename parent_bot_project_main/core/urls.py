from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('join/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', views.password_reset_view, name='password_reset'),
    path('model/', views.dodam_view, name='dodam'),
    path('api/nickname-check/', views.nickname_check, name='api_nickname_check'),
    path('api/email/send-code/', views.send_email_code, name='api_send_email_code'),
    path('api/email/verify-code/', views.verify_email_code, name='api_verify_email_code'),
    path('api/password-reset/send-code/', views.password_reset_send_code, name='api_password_reset_send'),
    path('api/password-reset/verify-code/', views.password_reset_verify_code, name='api_password_reset_verify'),
]