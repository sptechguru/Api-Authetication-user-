
from django.contrib import admin
from django.urls import include, path

# define Routesr
from rest_framework import routers
from quickstart import views

# authetication token
from rest_framework.authtoken.views import obtain_auth_token




router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)



admin.site.site_header =' API_DJANGO Rest_framework '
admin.site.site_title = 'PAL SAHAB '
admin.site.index_title = '??? ... SUPER DJANGO REST  FOR SPTECH PAL .... ???'




urlpatterns = [

    path('admin/', admin.site.urls),

# app installed snippets creted
    path('sp/', include('snippets.urls')),

# app installed crampp creted
    path('api/', include('crmapp.urls')),

# define Routesr
    path('sp/', include(router.urls)),
    
   
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

# authetication token

    path('rest-auth/', include('rest_auth.urls')),

    path('api/token/',obtain_auth_token,name='obtain-token')
    
]
