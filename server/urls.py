# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("auth/", include("auth.urls")),  # Including auth folder URLS
#     path(
#         "products/", include("products.urls")
#     ),  # Get all products from products directory
# ]


# ----------------

from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Single Ecommerce Server",
        default_version='v1',
        description="A single e-commerce server",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("auth.urls")),
    path("products/", include("products.urls")),
    path("cart/", include("cart.urls")),
    path("cart_item/", include("cart_item.urls")),
    path('order/', include("order.urls")),
    path('order_item/', include('order_item.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('wishlist_item/', include('wishlist_item.urls')),
    path('category/', include('category.urls')),
    path('user_metadata/', include('user_metadata.urls')),

    # Swagger documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
