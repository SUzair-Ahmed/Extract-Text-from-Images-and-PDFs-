from django.urls import path
from . import views

urlpatterns = [
    # path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('accounts/login/', views.CustomLoginView.as_view(), name='account_login'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.custom_logout, name='logout'),  # Custom logout view


]
