# nonprofit_site/urls.py

from django.contrib import admin
from django.urls import path, include
from builder import views as builder_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # This routes our custom 'accounts' pages (like signup)
    path('accounts/', include('accounts.urls')),
    
    # This routes Django's built-in auth URLs (login, logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # THE CHANGE IS HERE:
    # First, we define the main dashboard URL.
    path('dashboard/', builder_views.dashboard, name='dashboard'),
    
    # Second, we tell Django to include all other URLs from our builder app.
    # This will find the '/create/' URL we just made.
    path('dashboard/', include('builder.urls')),

    # This routes all our core pages (homepage, about, etc.)
    path('', include('core.urls')),
]