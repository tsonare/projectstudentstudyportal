from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"note", views.NoteViewSet)
router.register(r"homeworks", views.HomeworkViewSet)
router.register(r"todos", views.TodoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
