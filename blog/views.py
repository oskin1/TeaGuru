from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Tag


def postList(request):
    tag_filter = request.GET.get('tag_filter')
    tags = Tag.objects.all()
    if tag_filter:
        post_list = Post.objects.filter(active=True, tags__id=tag_filter)
    else:
        post_list = Post.objects.filter(active=True)
    limit = 8
    paginator = Paginator(post_list, limit)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)    
    template = loader.get_template('post_list.html')
    return HttpResponse(template.render({'posts':posts, 'tags':tags,}, request))
    
def postDetail(request, slug=None):
    post = Post.objects.get(slug=slug)
    template = loader.get_template('post_detail.html')
    return HttpResponse(template.render({'post':post}, request))    