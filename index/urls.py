from django.conf.urls import url

from index.views import Index, SignUpView

urlpatterns = [
    url('signup/', SignUpView.as_view(), name='signup'),
    url('', Index.as_view(), name='index'),
]