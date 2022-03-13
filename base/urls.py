from base.viewsets import VehicleViewSet, UserViewSet
from rest_framework import routers
from django.urls import path, include
from base.views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
	TokenRefreshView,
)


router = routers.SimpleRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'users', UserViewSet)
urlpatterns = router.urls

urlpatterns = [
    path('', include(urlpatterns)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
