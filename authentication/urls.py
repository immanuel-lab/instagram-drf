from django.urls import path
from .views import create_custom_user
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    # register
    path('register/', create_custom_user, name='create_custom_user'),

    # authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



    # login
      # path('login/', views.LoginView.as_view(), name='login'),

    # image upload and share
    # to get all images
    #  path('feed/', views.FeedView.as_view(), name='feed'),  
    
    #  for image upload
    # path('image/upload/', views.UploadImageView.as_view(), name='upload_image'),

    # path('image/<int:pk>/', views.ImageView.as_view(), name='image_detail'),

      path('images/', views.images_view, name='image_view'),  
        path('images/<int:pk>/comments/', views.update_comments, name='update_comments'),
        path('images/<int:pk>/', views.delete_image, name='delete_image'),
      
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


