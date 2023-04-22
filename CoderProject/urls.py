"""
URL configuration for CoderProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Games.views import index, PostList, PostDetail, PostCreate, PostUpdate, PostDelete, SignUp, Login, Logout, ProfileUpdate, MessageCreate, MessageDelete, MessageList, ProfileCreate, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Urls Genericas
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    #Urls de Posts
    path('post/list',PostList.as_view(), name='post-list'),
    path('post/<pk>/details',PostDetail.as_view(), name='post-details'),
    path('post/create',PostCreate.as_view(), name='post-create'),
    path('post/<pk>/update',PostUpdate.as_view(), name='post-update'),
    path('post/<pk>/dalete',PostDelete.as_view(), name='post-delete'),
    #Urls de Sigup
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    #Urls De profile
    path('profile/<pk>/update', ProfileUpdate.as_view(), name='profile-update'),
    path('profile/<pk>/create',ProfileCreate.as_view(), name='profile-create'),
    #Urls de Mensajes
    path('Message/create',MessageCreate.as_view(), name='message-create'),
    path('Message/list',MessageList.as_view(), name='message-list'),
    path('Message/<pk>/delete', MessageDelete.as_view(), name='message-delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
