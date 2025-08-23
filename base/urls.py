from django.urls import path, include
from . import views

urlpatterns = [
    path("accounts/",include('django.contrib.auth.urls')),
    path("home", views.home, name="home"),
    # path("dashboard/", views.dashboard, name="dashboard"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
   
]
