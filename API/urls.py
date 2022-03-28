from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# from rest_framework.authtoken.views import obtain_auth_token
# from .authentication import CustomAuthToken


router = routers.DefaultRouter()
router.register(r"note", views.NoteViewSet)
router.register(r"subject", views.SubjectViewSet)
router.register(r"homeworks", views.HomeworkViewSet)
router.register(r"todos", views.TodoViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Demo Project API",
      default_version='v1',
      description="This api helps to make notes, homework and todo.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="tsonare@bestpeers.com"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("api-token-auth/", CustomAuthToken.as_view()),
    # path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
