from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post/list.html'
    queryset = Post.published.all()
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post/detail.html'
    queryset = Post.published.all()

    def get_object(self, queryset=None):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        slug = self.kwargs.get('slug')

        queryset = queryset or self.queryset
        post = get_object_or_404(queryset,
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day,
                                 slug=slug)

        return post
