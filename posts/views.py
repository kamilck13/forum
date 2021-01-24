from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from posts.models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    login_url = 'login'


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    login_url = 'login'
    fields = ['discussion', 'body']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(PostCreate, self).form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    login_url = 'login'
    fields = ['discussion', 'body']

    def test_func(self):
        return self.request.user == self.get_object().created_by


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    login_url = 'login'
    success_url = reverse_lazy('category-list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user == self.object.created_by
