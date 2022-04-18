from django.urls import path
from .views import SignUpAPI, InferenceCnnAPI

urlpatterns = [
    path('sign-up', SignUpAPI.as_view()),
    path('inference/cnn', InferenceCnnAPI.as_view())
]