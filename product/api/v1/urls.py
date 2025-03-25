from rest_framework.routers import DefaultRouter

from product.api.v1.views import ProductViewSet

app_name = 'product'

router = DefaultRouter()
router.register(r'', ProductViewSet, basename='product')

urlpatterns = router.urls
