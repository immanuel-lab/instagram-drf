from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Chats(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"{self.owner}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Chat Message"
       