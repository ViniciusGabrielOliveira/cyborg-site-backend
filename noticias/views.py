import django_filters.rest_framework
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters


from noticias.serializers import UserSerializer, GroupSerializer, NoticiaSerializer
from noticias.models import Noticia


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

class DetalheList(generics.ListAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$tags', '$title']