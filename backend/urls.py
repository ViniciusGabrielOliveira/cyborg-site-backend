from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.urls import path, include

from noticias import views

router = routers.DefaultRouter()
router.register(r'noticias', views.NoticiaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path(r'detalhes/', views.DetalheList.as_view(), name="noticia-detail"),
    path('token-auth/', obtain_jwt_token),
    path('core/', include('core.urls'))
]
