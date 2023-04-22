from django.contrib import admin
from Games.models import Post, Profile, DM

#Modelos en el admin

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(DM)