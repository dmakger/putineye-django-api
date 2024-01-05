from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token"),
    path("api/refresh_token/", TokenRefreshView.as_view(), name="refresh_token"),

    path('api/user/', include('user.urls')),
    path('api/tg/', include('tg.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
