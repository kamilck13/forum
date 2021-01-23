from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView

from categories.models import Category


class CategoryListView(ListView):
    model = Category

class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CategoryCreate, self).form_valid(form)