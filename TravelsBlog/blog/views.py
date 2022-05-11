from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
def post_list(request):
    obj_list = Post.objects.all()
    paginator = Paginator(obj_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'posts': posts,
                                                   'page': page})

def post_detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post, slug=post_slug,
                             published__year=year,
                             published__month=month,
                             published__day=day)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post,
                                                     'form': form,
                                                     'comments': comments,
                                                     })

