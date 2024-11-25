from .serializers import UserSerializers, UserLoginSerializer
from .models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pms:dashboard')  # Redirect to the dashboard after successful login
        else:
            return render(request, 'account/login.html', {'error': 'Invalid username or password'})
    return render(request, 'account/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class AuthUserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_data = serializer.validated_data
            response = {
                'success': True,
                'message': 'User logged in successfully',
                'email': user_data['email'],
                'role': user_data['role']
            }
            return Response(response, status=status.HTTP_200_OK)
