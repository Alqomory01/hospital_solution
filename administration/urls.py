from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
from .views import RegisterView, RoleDashboardView
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"), 
    path('register/', RegisterView.as_view(), name='register'), 
    path('login/', TokenObtainPairView.as_view(), name='login'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('dashboard/', RoleDashboardView.as_view(), name='role_dashboard'),
]
