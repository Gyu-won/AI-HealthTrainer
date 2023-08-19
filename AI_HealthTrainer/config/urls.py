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
from AI_HealthTrainer import views as account_views
from django.contrib.auth import views as auth_views
from AI_HealthTrainer.views import CustomLoginView, HomeView, CustomLogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("show",views.show),
    path('', views.index, name='index'),
    path('video_feed/', views.webcam, name='webcam'),
    # path("insert", views.insert, name='insert'),
    path('exercise/', views.exercise_list, name='exercise'),
    path('exercise/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('exercise/create/', views.exercise_create, name='exercise_create'),
    path('exercise/<int:pk>/update/', views.exercise_update, name='exercise_update'),
    path('exercise/<int:pk>/delete/', views.exercise_delete, name='exercise_delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
    # path('register/', account_views.Register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    
]
