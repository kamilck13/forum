from django.conf.urls import url

from discussions.views import DiscussionListView, DiscussionCreate, DiscussionDetailView, DiscussionUpdate, DiscussionDelete

urlpatterns = [
    url(r'^$', DiscussionListView.as_view(), name='discussion-list'),
    url(r'^(?P<pk>\d+)/$', DiscussionDetailView.as_view(), name='discussion-detail'),
    url(r'discussion/add/$', DiscussionCreate.as_view(), name='discussion-add'),
    url(r'discussion/(?P<pk>[0-9]+)/$', DiscussionUpdate.as_view(), name='discussion-update'),
    url(r'discussion/(?P<pk>[0-9]+)/delete/$', DiscussionDelete.as_view(), name='discussion-delete'),
]