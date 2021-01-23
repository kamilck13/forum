from django.conf.urls import url

from categories.views import CategoryListView, CategoryCreate, CategoryDetailView, CategoryUpdate, CategoryDelete

urlpatterns = [
    url(r'^$', CategoryListView.as_view(), name='category-list'),
    url(r'^(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'category/add/$', CategoryCreate.as_view(), name='category-add'),
    url(r'category/(?P<pk>[0-9]+)/$', CategoryUpdate.as_view(), name='category-update'),
    url(r'category/(?P<pk>[0-9]+)/delete/$', CategoryDelete.as_view(), name='category-delete'),
]