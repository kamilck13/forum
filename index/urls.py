from django.conf.urls import url

from index.views import Index

urlpatterns = [
    url('', Index.as_view(), name='index'),
]