"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from basic import models, views
from django.conf import settings
from django.conf.urls.static import static
from basic.models import *
from rest_framework import routers, serializers, viewsets




# Serializers define the API representation.
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ["name","phone","email","password"]  

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'home', UserViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.register, name="register"), 
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path("", views.cc, name="home"), 
    
    # path('customer/', v.showf, name='customer'),

    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    

    path('s', include("basic.urls")),


    path('p/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)