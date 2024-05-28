from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import User
from users.serializers import UserSerializer
# Create your views here.

class LoginView(APIView):
    def post(self, request):
        user= get_object_or_404(User,username=request.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        serializer=UserSerializer(instance=user)
        return Response({
            'token': token.key,
            'user': serializer.data,
            }, status=status.HTTP_200_OK)
        

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.headers) 
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()

        return Response({'detail': 'Successfully logged out.'})