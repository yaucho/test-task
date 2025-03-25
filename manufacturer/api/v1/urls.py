from rest_framework.routers import DefaultRouter

from manufacturer.api.v1.views import ManufacturerViewSet

app_name = 'manufacturer'

router = DefaultRouter()
router.register(r'', ManufacturerViewSet, basename='manufacturer')

urlpatterns = router.urls
