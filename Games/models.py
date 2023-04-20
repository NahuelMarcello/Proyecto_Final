from django.db import models

class Post(models.Model):
    game_name = models.CharField(max_length=30)
    game_type = models.CharField(max_length=80)
    game_description = models.CharField(max_length=120)
    game_note = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.id} - {self.game_name} - {self.game_type}"


