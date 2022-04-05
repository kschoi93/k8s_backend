from django.urls import path
from .views import SignUpAPI

urlpatterns = [
    path('sign-up', SignUpAPI.as_view())
]