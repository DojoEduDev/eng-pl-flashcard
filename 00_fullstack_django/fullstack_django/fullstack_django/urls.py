from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
# from rest_framework.routers import DefaultRouter # will be used in FlashCards app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redic'),
    path('api/v1/',
        # register APPs URLs:
        include([
            path('words/', include('words.urls')),
            path('flashcards/', include('flashcards.urls')),
        ])
    ),
]
