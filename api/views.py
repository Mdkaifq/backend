from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

@api_view(['POST'])
@permission_classes([AllowAny])
def registerAsUser(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

 
@api_view(['POST'])
@permission_classes([AllowAny])
def registerAsAdmin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_superuser(username=username, password=password)
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

 
# Login user and return tokens
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.filter(username=username).first()

    if user and user.check_password(password):
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'userId': str(user.pk)
        })
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submitAssignment(request):
    
    if not User.objects.filter(username=request.data.get('userId')).exists():
        return Response("Incorrect userId, your username is your userId", status=status.HTTP_400_BAD_REQUEST)
    if not User.objects.get(username=request.data.get('admin')).is_superuser:
        return Response(f"{request.data.get('admin')} is not an admin", status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.get(username=request.data.get('userId'))
    obj = Assignments.objects.create(userId = user, task=request.data.get('task'), admin = request.data.get('admin') )
    obj.save()
    serializer = AssignmentSerializer(obj)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAdmins(request):
    obj = User.objects.filter(is_superuser=True)
    serializer = AdminSerializer(obj, many=True)
    admins = []
    for i in serializer.data:
        admins.append(i['username'])
    return Response(admins)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getAssignments (request):
    if not User.objects.get(username=str(request.user)).is_superuser:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    obj = Assignments.objects.filter(admin = request.user)
    serializer = AssignmentSerializer(obj, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def acceptAssignment (request, pk):
    obj = Assignments.objects.get(id=pk)
    obj.status = "Accepted"
    obj.save()
    serializer = AssignmentSerializer(obj)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def rejectAssignment (request, pk):
    obj = Assignments.objects.get(id=pk)
    obj.status = "Rejected"
    obj.save()
    serializer = AssignmentSerializer(obj)
    return Response(serializer.data)
