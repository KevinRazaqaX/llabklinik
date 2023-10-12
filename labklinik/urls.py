"""labklinik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# project/urls.py

from django.contrib import admin
from django.urls import path, include

from . import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base_view, name='base'),  # Example home view from your app
    path('login/', views.user_login, name='login'),  # Login view from your app
    path('register/', views.register, name='register'),  # Register view from your app
    path('logout/', views.custom_logout, name='logout'),
    path('tasklist', views.base_view, name='task_list'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('task/<int:task_id>/', views.task_details, name='task_details'),
    # Add other URL patterns as needed
]
