from django.urls import path, include
from .views import HelloApiView, HelloViewset

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewset, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('', include(router.urls))
]
