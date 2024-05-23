from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135521ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135521", Testconnectors135521ViewSet, basename="testconnectors135521"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
