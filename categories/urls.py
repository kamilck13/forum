from django.conf.urls import url

from categories.views import CategoryListView, CategoryCreate

urlpatterns = [
    url(r'^$', CategoryListView.as_view(), name='category-list'),
    url(r'note/add/$', CategoryCreate.as_view(), name='category-add'),
]