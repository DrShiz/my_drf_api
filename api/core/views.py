from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PostSerializer
from rest_framework.response import Response
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]
