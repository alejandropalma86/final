from django.shortcuts import render, get_object_or_404
from django.views import View
from taggit.models import Tag
from .models import Post


class BlogView(View):
    def get(self, request):
        template_name = 'blog/blog.html'
        context = dict(
        posts = Post.objects.all(), 
        )
        return render(request, template_name, context)

class TagView(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        common_tags = Post.tags.most_common()[:4]
        posts = Post.objects.filter(tags=tag)
        context = {
            'tag':tag,
            'common_tags':common_tags,
            'posts':posts,
        }
        return render(request, 'blog/blog.html', context)

    