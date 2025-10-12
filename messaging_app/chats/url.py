from django.contrib import admin
from django.urls import path, include
from chats import auth  # ✅ corrected

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

CustomTokenObtainPairView = TokenObtainPairView.as_view()
CustomTokenRefreshView = TokenRefreshView.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', CustomTokenObtainPairView, name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView, name='token_refresh'),
    path('api/chats/', include('chats.urls')),
]
