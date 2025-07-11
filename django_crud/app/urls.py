from django.contrib import admin
from django.urls import path, include
from .views import EventViewSet

urlpatterns = [
    path("api/", EventViewSet.as_view({"post": "create", "get": "list"}), name="apis"),
    path(
        "api/<int:pk>",
        EventViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
