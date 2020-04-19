from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from noticias import views

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'noticias', views.NoticiaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path(r'detalhes/', views.DetalheList.as_view(), name="noticia-detail")
]
