from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/auth/', include('rest_auth.urls')),
    path('api/accounts/auth/refresh_token/', refresh_jwt_token),
    path('api/accounts/registration/', include('rest_auth.registration.urls')),
    # path('api/hangman/', include('hangman.urls')),
]
