from django.shortcuts import render
from rest_framework import viewsets

from apps.cast.serializers import CharacterSerializer
from apps.cast.models import Character


class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()
