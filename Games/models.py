from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    game_name = models.CharField(max_length=30)
    game_type = models.CharField(max_length=80)
    game_description = models.CharField(max_length=120)
    game_note = models.CharField(max_length=15)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="owner")
    images = models.ImageField(upload_to="posts", null=True, blank=True) 
    
    def __str__(self):
        return f"{self.id} - {self.game_name} - {self.game_type}"


