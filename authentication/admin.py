from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Image


admin.site.register(CustomUser)

admin.site.register(Image)


