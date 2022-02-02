from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cast/', include("apps.cast.urls", namespace="cast")),
]
