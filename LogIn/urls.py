from django.urls import include,path
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, AuthenticationForm, PasswordChangeForm, PasswordResetForm)

app_name = 'LogIn'


urlpatterns = [
    path('', include('django.contrib.auth.urls'))
]
