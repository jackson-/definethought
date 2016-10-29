from django.conf.urls import url
from blog.views import PostList, PostDetail

urlpatterns = [
    url(r'^(?P<slug>.+)', PostDetail.as_view()),
    url(r'^', PostList.as_view()),
]