from django.contrib import admin
from django.urls import path,include
from . import views
from account.views import SignUp
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm


urlpatterns = [
    path("" , views.index , name = "index"),
    path('signup/', SignUp.as_view(), name='signup'),
        # Login and Logout
    
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html',authentication_form = LoginForm),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='change-password.html',form_class =MyPasswordChangeForm,success_url = '/',),name='change_password'),


    path('password-reset/', auth_views.PasswordResetView.as_view(template_name ='password_reset.html',form_class = MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name ='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class = MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

]
