from django.shortcuts import render

# Create your views here.

from rest_framework import generics
#from rest_framework.permissions import IsAuthenticated
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer, ClientDetailSerializer
from django.contrib.auth.models import User


class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
   
   # permission_classes = [IsAuthenticated]


class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    #permission_classes = [IsAuthenticated]


class UserAssignedProjectsView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.projects.all()

