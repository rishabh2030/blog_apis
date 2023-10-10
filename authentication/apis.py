from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer,LoginSerializers
from rest_framework.permissions import IsAuthenticated
from helper.functions import *
import keys,messages
from django.contrib.auth import authenticate
from rest_framework.views import APIView

class RegisterView(generics.CreateAPIView):
    """ 
    API to Register User
    
    HEAD PARAM: None
    PATH PARAMS: None
    QUERYSTRING PARAMS: None
    API RESPONSE: Dictionary
    
    """
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, refresh_token = user.get_tokens()
        token = {"access_token": token, "refresh_token": refresh_token}
        return Response(ResponseHandling.success_response_message(messages.REGISTRACTION_USER, token), status=status200)

class LoginView(generics.CreateAPIView):

    """ 
    API to Login User
    
    HEAD PARAM: None
    PATH PARAMS: None
    QUERYSTRING PARAMS: None
    API RESPONSE: Dictionary
    
    """
    serializer_class = LoginSerializers
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            errors = serializer.errors
            err = error_message_function(errors)
            return Response(ResponseHandling.failure_response_message(err, {}), status=status400)
        mobile = request.data[keys.MOBILE]
        password = request.data[keys.PASSWORD]
        if not mobile and password:
            return Response(ResponseHandling.failure_response_message(messages.PROVIDE_FIELDS, ""), status=status400)
        user = UserFunctions.get_user(mobile)
        token, refresh_token = user.get_tokens()
        token = {"access_token": token, "refresh_token": refresh_token}
        return Response(ResponseHandling.success_response_message(messages.LOGIN_SUCCESS, token), status=status200)
