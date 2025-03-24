from rest_framework.routers import DefaultRouter

from contract.api.v1.views import ContractViewSet

app_name = 'contract'

router = DefaultRouter()
router.register(r'', ContractViewSet, basename='contract')

urlpatterns = router.urls
