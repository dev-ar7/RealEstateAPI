from django.contrib import admin
from django.urls import path, include
# from rest_framework import permissions

# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view 


# schema_view = get_schema_view(
#     openapi.Info(
#         title='RealEstate API',
#         default_version='v1',
#         description='Official API documentation of RealEstate',
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="arnab.gupta.ar7@gmail.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )


urlpatterns = [
    path('api/v1/', 
        include([
            path('admin/', admin.site.urls),
            # path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
            path('', include('accounts.urls')),
            path('contact/', include('contacts.urls')),
            path('listing/', include('listing.urls')),
        ])
    ),
]
