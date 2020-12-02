import django_filters.rest_framework
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import AllowAny
from noticias.serializers import UserSerializer, GroupSerializer, NoticiaSerializer
from noticias.models import Noticia
from noticias.permissions import IsAdminUser, IsLoggedInUserOrAdmin


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all().order_by('-classification')
    serializer_class = NoticiaSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        elif self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH' or self.request.method == 'HEAD' or self.request.method == 'OPTIONS' or self.request.method == 'DELETE':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class DetalheList(generics.ListAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$tags', '$title']

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        elif self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH' or self.request.method == 'HEAD' or self.request.method == 'OPTIONS' or self.request.method == 'DELETE':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]