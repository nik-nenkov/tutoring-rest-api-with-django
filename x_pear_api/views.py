from django.shortcuts import render
from rest_framework import viewsets

from .models import Actor, Transporter, Load, Storage
from .serializers import ActorSerializer, TransporterSerializer, LoadSerializer, StorageSerializer


def index(request):
    return render(request, 'index.html')


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class TransporterViewSet(viewsets.ModelViewSet):
    queryset = Transporter.objects.all()
    serializer_class = TransporterSerializer


class LoadViewSet(viewsets.ModelViewSet):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
