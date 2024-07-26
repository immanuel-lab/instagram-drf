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


# class FeedView(generics.ListAPIView):
#     serializer_class = ImageSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Image.objects.all()
    
# class UploadImageView(generics.CreateAPIView):
#     serializer_class = ImageSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class ImageView(generics.RetrieveAPIView):
#     serializer_class = ImageSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Image.objects.all()


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
        
    
    

   
   
   
    # elif request.method == 'DELETE':
    #     if not pk:
    #         return Response({'detail': 'Method "DELETE" not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     image = get_object_or_404(Image, pk=pk)
    #     if image.owner != request.user:
    #         return Response(status=status.HTTP_403_FORBIDDEN)
    #     image.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    

 # Assuming you have a serializer for the User model
# from .serializers import UserSerializer
# @permission_classes([IsAuthenticated])
# @api_view(['GET'])
# def request_methods(request):
#      serializer = UserSerializer(request.user)
#      return Response(serializer.data, status=status.HTTP_200_OK)

  
  


