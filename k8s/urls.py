from django.urls import path
from .views import GetDataAPI, SignUpAPI

urlpatterns = [
    path('sign-up', SignUpAPI.as_view())
]