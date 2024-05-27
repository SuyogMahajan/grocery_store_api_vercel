from django.urls import path
from .views import *

from drf_yasg.views import get_schema_view

from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Your API",
      default_version='v1',
      description="Your API description",
      terms_of_service="https://www.yourapp.com/terms/",
      contact=openapi.Contact(email="contact@yourapp.com"),
      license=openapi.License(name="Your License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('category', CategoryApiView.as_view()),
    path('category/<int:pk>', CategoryDetailApiView.as_view()),

    path('products', ProductsApiView.as_view()),
    path('products/<int:pk>', ProductsDetailApiView.as_view()),

    path('manufacturer', ManufacturerApiView.as_view()),
    path('manufacturer/<int:pk>', ManufacturerDetailApiView.as_view()),

    path('сountry', CountryApiView.as_view()),
    path('сountry/<int:pk>', CountryDetailApiView.as_view()),

    path('orders', OrderApiView.as_view()),
    path('orders/<int:pk>', OrderDetailApiView.as_view()),


    path('sign_in', AuthApiView.as_view()),
    path('sign_out', LogOutApiView.as_view()),
    path('profile', ProfileApiView.as_view()),
    path('sign_up', RegistrationApiView.as_view()),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
