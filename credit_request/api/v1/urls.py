from rest_framework.routers import DefaultRouter

from credit_request.api.v1.views import CreditRequestViewSet

app_name = 'credit_request'

router = DefaultRouter()
router.register(r'', CreditRequestViewSet, basename='credit_request')

urlpatterns = router.urls
