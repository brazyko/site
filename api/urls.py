from django.urls import path,include
from rest_framework import routers
from .views import *

name = 'api'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet),
router.register(r'orders',OrderViewSet),
router.register(r'parts',ProductViewSet),

urlpatterns = [
    path('', include(router.urls)),
]