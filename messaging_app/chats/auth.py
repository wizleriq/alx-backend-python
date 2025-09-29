from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

CustomTokenObtainPairView = TokenObtainPairView.as_view()
CustomTokenRefreshView = TokenRefreshView.as_view()
