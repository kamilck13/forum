from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from categories.models import Category
from discussions.models import Discussion


class CategoryListView(ListView):
    model = Category

class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['discussions'] = Discussion.objects.filter(categories=self.get_object().pk)
        return context

class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    login_url = 'login'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CategoryCreate, self).form_valid(form)

class CategoryUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    login_url = 'login'
    fields = ['title', 'body']

    def test_func(self):
        return self.request.user == self.get_object().created_by

class CategoryDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    login_url = 'login'
    success_url = reverse_lazy('category-list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user == self.object.created_by