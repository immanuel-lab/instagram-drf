from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Image


admin.site.register(CustomUser)

# admin.site.register(Image)




class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner','image', 'description', 'likes', 'comments')

admin.site.register(Image, ImageAdmin)


