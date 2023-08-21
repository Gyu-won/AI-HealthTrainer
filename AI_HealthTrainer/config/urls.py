"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from AI_HealthTrainer import views
from django.contrib.auth import views as auth_views
from AI_HealthTrainer.views import CustomLoginView, HomeView, CustomLogoutView, RegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('video_feed/', views.webcam, name='webcam'),
    path('home/exercise/', views.exercise_list, name='exercise_list'),
    path('home/exercise/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('home/exercise/create/', views.exercise_create, name='exercise_create'),
    path('home/exercise/<int:pk>/update/', views.exercise_update, name='exercise_update'),
    path('home/exercise/<int:pk>/delete/', views.exercise_delete, name='exercise_delete'),
    path('home/goal/', views.goal_list, name='goal_list'),
    path('home/goal/create/', views.goal_create, name='goal_create'),
    path('home/goal/<int:pk>/', views.goal_detail, name='goal_detail'),
    path('home/goal/<int:pk>/update/', views.goal_update, name='goal_update'),
    path('home/goal/<int:pk>/delete/', views.goal_delete, name='goal_delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
]
