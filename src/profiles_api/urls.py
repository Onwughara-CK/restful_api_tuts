from django.urls import path, include
from .views import HelloApiView

urlpatterns = [
    path('hello-view/', HelloApiView.as_view())
]
