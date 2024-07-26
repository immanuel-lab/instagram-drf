from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, full_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not user_name:
            raise ValueError('The Username field must be set')
        if not full_name:
            raise ValueError('The Full Name field must be set')
        if not password:
            raise ValueError('The Password field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, user_name, full_name, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=150)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'full_name',]

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


# model for image

from django.conf import settings

class Image(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.owner}"

  







