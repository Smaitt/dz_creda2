from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_issue/', views.create_issue, name='create_issue'),
    path('issue_list/', views.issue_list, name='issue_list'),
    path('issue/<int:issue_id>/', views.issue_detail, name='issue_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='helpdesk/login.html'), name='login'),
]
