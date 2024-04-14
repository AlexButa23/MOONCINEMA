from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r"filme", filmeViewSet)
router.register(r"rezervare", rezervareViewSet)
router.register(r"recomandari",recomandariViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
