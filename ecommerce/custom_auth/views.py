

from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .serializers import UserSerializer


class RegisterView(APIView):
    
    def post(self , request):

        
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                user = serializer.save()
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "status":"success" ,
                        'user_id' :user.id , 
                        'refresh': str(refresh),
                        'access': str(refresh.access_token)
                    },status=status.HTTP_201_CREATED
                    )
            except Exception as save_error:
                return Response({'message':'failure',
                             'error':str(save_error)})
        return Response(
                {
                    "status":"failure" ,
                    "message" : "Record already exist.",
                    "error":serializer.errors
                },status=status.HTTP_409_CONFLICT)
        