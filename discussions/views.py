from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from discussions.models import Discussion
from posts.models import Post


class DiscussionListView(ListView):
    model = Discussion


class DiscussionDetailView(LoginRequiredMixin, DetailView):
    model = Discussion
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(DiscussionDetailView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(discussion=self.get_object().pk)
        return context


class DiscussionCreate(LoginRequiredMixin, CreateView):
    model = Discussion
    login_url = 'login'
    fields = ['categories', 'title']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(DiscussionCreate, self).form_valid(form)


class DiscussionUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Discussion
    login_url = 'login'
    fields = ['title']

    def test_func(self):
        return self.request.user == self.get_object().created_by


class DiscussionDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Discussion
    login_url = 'login'
    success_url = reverse_lazy('discussion-list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user == self.object.created_by
