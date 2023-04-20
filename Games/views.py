from django.shortcuts import render
from Games.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    return render(request, "Games/index.html")

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields= '__all__'

class PostUpdate(UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields= '__all__'

class PostDelete(DeleteView):
     model = Post
     success_url = reverse_lazy("post-list")

