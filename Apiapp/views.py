from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
# from .models import Category, Book, Product, Cart
from .serializers import RegistrationSerializer,AdvisorSerializer,BookSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import uuid
from .models import Advisor




class RegistrationAPIView(generics.ListCreateAPIView):
    
    queryset = User.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = RegistrationSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)

class AdvisorViewSet(generics.ListCreateAPIView):
    queryset=Advisor.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class=AdvisorSerializer

class ViewSet(generics.ListCreateAPIView):
    queryset=Advisor.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class=BookSerializer    