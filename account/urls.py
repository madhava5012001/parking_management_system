# account/urls.py
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'account'

urlpatterns = [
    # API-based JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Account-related views (function-based views)
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
