
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views





urlpatterns = [
    
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)










# old urls
# from django.urls import path
# from snippets import views

# # from rest_framework import routers
# # router = routers.DefaultRouter()
# # router.register(r'users', views.UserViewSet)


# urlpatterns = [

#     path('snippets/', views.snippet_list),  
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]