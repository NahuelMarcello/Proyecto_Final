from django.shortcuts import render
from Games.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Games.forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, "Games/index.html")

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields= '__all__'

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields= '__all__'
     
    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Post.objects.filter(owner=user_id, id=post_id).exists()
    def handle_no_permission(self):
        return render(self.request, "Games/not_found.html")


class PostDelete(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
     model = Post
     success_url = reverse_lazy("post-list")
     
     def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Post.objects.filter(owner=user_id, id=post_id).exists()
     def handle_no_permission(self):
        return render(self.request, "Games/not_found.html")

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('post-list')


class Login(LoginView):
    next_page = reverse_lazy('post-list')

class Logout(LogoutView):
   template_name = 'registration/logout.html'
