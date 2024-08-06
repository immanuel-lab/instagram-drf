from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer


@api_view(['POST'])
def create_custom_user(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    # login view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    



# image creation for authenticated user

from rest_framework import generics, permissions
from .models import Image
from .serializers import ImageSerializer






from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def images_view(request):
    if request.method == 'GET':
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():    
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_comments(request, pk):
    try:
        image = Image.objects.get(pk=pk)
        # if image.comments.owner != request.user:
            # return Response({'error': 'On ly the owner of comments can update comments'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ImageSerializer(image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

   
   
@api_view(['DELETE'])
def delete_image(request, pk):
    try:
        image = Image.objects.get(pk=pk)
        if image.owner != request.user:
            return Response({'error': 'Only the owner of the image can delete it'}, status=status.HTTP_403_FORBIDDEN)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

  
  


