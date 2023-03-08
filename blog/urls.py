from django.urls import path

from blog.views import PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('page/<int:page>/', PostListView.as_view(), name='paginator'),

    path('<int:year>/<int:month>/<int:day>/<slug:slug>', PostDetailView.as_view(), name='post_detail')

]
