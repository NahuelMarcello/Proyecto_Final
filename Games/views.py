from django.shortcuts import render
from Games.models import Post, Profile, DM
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from  .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def about(request):
    return render(request, "Games/about.html")

def index(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "Games/index.html", context)

#CBV para posts
class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields= ['game_name','game_type','game_description','game_note','images']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields= ['game_name','game_type','game_description','game_note','images']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
     
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

#CBV para SignUp

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')

class Login(LoginView):
    next_page = reverse_lazy('index')

class Logout(LogoutView):
   template_name = 'registration/logout.html'

#CBV para Perfil

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['steam_id', 'Contact', 'images']
    success_url = reverse_lazy('index')  
    template_name = 'profile/profile_form.html'
    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)
    
    def handle_no_permission(self):
        return render(self.request, "Games/not_found.html")

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['steam_id', 'Contact', 'images']
    success_url = reverse_lazy('index')  
    template_name = 'profile/profile_create.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def handle_no_permission(self):
        return render(self.request, "Games/not_found.html")

#CBV para mensajes

class MessageCreate(CreateView):
    model = DM
    fields = '__all__'
    template_name = 'Mensajes/DM_form.html'
    success_url = reverse_lazy('post-list')

class MessageList(LoginRequiredMixin, ListView):
    model = DM
    template_name = 'Mensajes/DM_list.html'
    context_object_name = "mensajes" 

    def get_queryset(self):
        return DM.objects.filter(addressee = self.request.user.id).all()

class MessageDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DM
    template_name = 'Mensajes/DM_confirm_delete.html'
    success_url = reverse_lazy('message-list')

    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return DM.objects.filter(addressee = user_id).exists()