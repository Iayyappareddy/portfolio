from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Contact, name='home'),
    path('messages/', views.message_list, name='message_list'),
    path('login/',auth_views.LoginView.as_view(template_name='adminp/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('messages/<int:pk>/',views.del_message,name='del_message'),
]