from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from myappback.api.resources import CategoryActivityModelViewSet, DoctorsModelViewSet


router = routers.DefaultRouter()
router.register('category-activity', CategoryActivityModelViewSet)
router.register('doctors', DoctorsModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]