from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework import viewsets
from .serializers import *
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

# Create your views here.

class UserViewSet(viewsets.GenericViewSet, CreateModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

class ClientViewSet(viewsets.GenericViewSet, CreateModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = ClientSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        logout(request)
        return Response(status=204)