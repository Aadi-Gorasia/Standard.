# builder/urls.py

from django.urls import path
from . import views

# This 'app_name' helps Django differentiate URLs.
app_name = 'builder'

urlpatterns = [
    # This creates the URL pattern for our website creation page.
    # Because of the rule in our main urls.py, the final URL will be "/dashboard/create/".
    path('create/', views.create_website_view, name='create_website'),
]