from django.db.models import base
from django.urls import include, path
from rest_framework import routers

from .views import ProductViewSet, UserApiView

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet, basename='product')
urlpatterns = [
  path('user/',  UserApiView.as_view()),
]

urlpatterns += router.urls
