"""vehicles_api URL Configuration
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Vehicles API",
      default_version='v1',
      description="__Users__\n \
        * Anyone can create user.\n \
        * Deleting a user will delete related vehicles.\n \
        * A user can only delete his own account.\n \
        * After deleting an account don't forget to remove authorization \
        header credentials or request will return *401 Error: Unauthorized*. \
        Removing auth token is also normally what the client will do on logout \
        or when the token refresh request response status code is not 200 (successful).\n \
        __Vehicles__\n \
        * Only authenticated user can create vehicles.\n \
        * Only owners of a vehicle can update/create/delete the vehicle.\n \
        __Pagination__\n \
        * Default pagination size is set to 5.\n \
        * API endpoint for ```/vehicles/``` (GET) include query parameter ```page_size``` that allows the client to set the page size on a per-request basis.\n \
        * Accept a page number in the request query parameters. url example : ```/api/vehicles/?page=1&page_size=10```.\n \
        * Default ordering is using created date value. Available keys for ordering are ```price``` and ```created```.\n \
        * Ordering is parameterizable with ```ordering``` query parameter. example : ```/api/vehicles/?ordering=-price```\n \
        __Authentication__\n \
        Usually, JWT authentication can be used in RESTful APIs. For production it is highly recommended to use HTTPS with a valid SSL certificate.\n \
        Expected flow for creating/editing/deleting vehicle with __JWT authentication__ : \n \
        * Create a user, endpoint ```/users/``` (POST)\n \
        * Get access/refresh token ```/token/``` (POST). Default lifetime is 5 minutes but can be modified in /vehicles_api/local_settings.py config file of the project.\n \
        * Authorize POST, DELETE and PUT/PATCH requests types by adding the token value in the request header.\n \
        Format is : __Authorization: \<type\> \<credentials\>__ with type __Bearer__ (do not forget to include it !)\n \
    ",
      contact=openapi.Contact(email="lucas.bromblet@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # Documentation
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Admin
    path('admin/', admin.site.urls),

    # Include urls apps
    path('api/', include('base.urls'))
]
