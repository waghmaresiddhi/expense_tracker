from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Route for the root URL
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # Include your app URLs here
]
