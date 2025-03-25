from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/v1/contracts/', include('contract.api.v1.urls')),
    path('api/v1/products/', include('product.api.v1.urls')),
    path('api/v1/manufacturers/', include('manufacturer.api.v1.urls')),
    path('api/v1/credit-requests/', include('credit_request.api.v1.urls')),
]
