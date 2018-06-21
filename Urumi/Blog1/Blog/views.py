from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from Blog.models import Post


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


def post_list(request):
    posts_all = Post.published.all()
    paginator = Paginator(posts_all, 3)  # 3 page in
    pageNum = request.GET.get('page')
    try:
        posts = paginator.page(pageNum)
    except PageNotAnInteger:
        posts = paginator.page(1)  # not a integer get first page
    except EmptyPage:
        # pageNum out of range show last page
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': pageNum, 'posts': posts})
