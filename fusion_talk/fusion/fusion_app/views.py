from django.shortcuts import render
def login(request):
    return render(request, 'login.html')   
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
#User Authentication and Profile Management:
class RegisterUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({"message": "User registered successfully", "user_id": user.id}, status=status.HTTP_201_CREATED)


class LoginUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"message": "Login successful", "token": token.key}, status=status.HTTP_200_OK)


class LogoutUserView(APIView):
    def post(self, request):
        token = request.auth
        if token:
            token.delete()
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        return Response({"error": "No token provided"}, status=status.HTTP_400_BAD_REQUEST)


class GetUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        profile_data = {
            "username": user.username,
            "email": user.email,
            "display_name": user.first_name,
            "profile_picture": None  # Add logic if profile pictures are supported
        }
        return Response(profile_data, status=status.HTTP_200_OK)


class UpdateUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        display_name = request.data.get('display_name')
        email = request.data.get('email')

        if display_name:
            user.first_name = display_name
        if email:
            user.email = email
        user.save()

        return Response({"message": "Profile updated successfully"}, status=status.HTTP_200_OK)
    
#Group Management







#Chat Functionality





#Gemini API Integration





#Private g char




#Scalability and extendibility







#Notification 



