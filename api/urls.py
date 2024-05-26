from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


SchemaView = get_schema_view(
    info=openapi.Info(
        title='Store',
        default_version='v1.0',
        description='This is an electronic grocery store',
        terms_of_service='',
        contact=openapi.Contact(name='Suyog Mahajan', url='', email='SuyogMahajan2111@gmail.com'),
        license=openapi.License(name='JustCode', url='')
    ),

    patterns=[
        path('', include('shop.urls')),
    ],
    public=True,
    permission_classes=[AllowAny, ]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shop.urls')),
    # path('', include('example.urls')),
    path('swagger/', SchemaView.with_ui()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
