from django.conf.urls import url

from posts.views import PostListView, PostCreate, PostDetailView, PostUpdate, PostDelete

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'post/add/$', PostCreate.as_view(), name='post-add'),
    url(r'post/(?P<pk>[0-9]+)/$', PostUpdate.as_view(), name='post-update'),
    url(r'post/(?P<pk>[0-9]+)/delete/$', PostDelete.as_view(), name='post-delete'),
]