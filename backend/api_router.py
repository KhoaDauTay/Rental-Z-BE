from rest_framework import routers

from core.views import UserViewSet
from house.views import HouseViewSet, HouseTypeViewSet

router = routers.SimpleRouter()
router.register('houses/house-types', HouseTypeViewSet, basename='house_types')
router.register('houses', HouseViewSet, basename='houses')
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls
