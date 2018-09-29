from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View

from .models import Post,Category
from django.utils.timezone import now
from urllib.parse import quote_plus
from .forms import PostForm

# Create your views here.
def index(request):
    rank_1=Post.objects.rank_1()
    recent_post=Post.objects.all().order_by('-date')[:3]
    categories=Category.objects.all()
    dictionary = {}
    for category in categories:
        post_list=Post.objects.filter(category=category).order_by('-date')[:4]
        dictionary[category]=post_list
    popular_post=Post.objects.filter(rating='3').order_by('-date')[:5]
    trending_post=Post.objects.filter(rating='4').order_by('-date')[:5]
    return render(request, 'post/index.html',{'now':now(),'rank_1':rank_1,'recent_post':recent_post,
                                              'dictionary':dictionary,'popular_post':popular_post,
                                              'trending_post':trending_post,})

def Indian_News(request):
    category = Category.objects.get(category='Indian News')
    post_list = Post.objects.filter(category=category).order_by('-date')
    popular_post = Post.objects.filter(rating='3').order_by('-date')[:5]
    trending_post = Post.objects.filter(rating='4').order_by('-date')[:5]
    return render(request, 'post/category_three.html', {'now':now(),'post_list': post_list,
                                                        'category':category,'popular_post':popular_post,
                                                        'trending_post':trending_post,})

def World_News(request):
    category = Category.objects.get(category='World News')
    post_list = Post.objects.filter(category=category).order_by('-date')
    popular_post = Post.objects.filter(rating='3').order_by('-date')[:5]
    trending_post = Post.objects.filter(rating='4').order_by('-date')[:5]
    return render(request, 'post/category_three.html',{'now': now(), 'post_list': post_list,
                                                       'category': category, 'popular_post': popular_post,
                                                       'trending_post': trending_post,})
def Economics(request):
    category = Category.objects.get(category='Economics')
    post_list = Post.objects.filter(category=category).order_by('-date')
    popular_post = Post.objects.filter(rating='3').order_by('-date')[:5]
    trending_post = Post.objects.filter(rating='4').order_by('-date')[:5]
    return render(request, 'post/category_three.html',
                  {'now': now(), 'post_list': post_list, 'category': category, 'popular_post': popular_post,
                   'trending_post': trending_post,})

def Sports(request):
    category = Category.objects.get(category='Sports')
    post_list = Post.objects.filter(category=category).order_by('-date')
    popular_post = Post.objects.filter(rating='3').order_by('-date')[:5]
    trending_post = Post.objects.filter(rating='4').order_by('-date')[:5]
    return render(request, 'post/category_three.html',
                  {'now': now(), 'post_list': post_list, 'category': category, 'popular_post': popular_post,
                   'trending_post': trending_post,})

def Entertainment(request):
    category=Category.objects.get(category='Entertainment')
    post_list = Post.objects.filter(category=category).order_by('-date')
    popular_post = Post.objects.filter(rating='3').order_by('-date')[:5]
    trending_post = Post.objects.filter(rating='4').order_by('-date')[:5]
    return render(request, 'post/category_three.html',
                  {'now': now(), 'post_list': post_list, 'category': category, 'popular_post': popular_post,
                   'trending_post': trending_post,})

def Technology(request):
    category = Category.objects.get(category='Technology')
    post_list = Post.objects.filter(category=category).order_by('-date')
    popular_post = Post.objects.filter(rating='3').order_by('-date')[:5]
    trending_post = Post.objects.filter(rating='4').order_by('-date')[:5]
    return render(request, 'post/category_three.html',
                  {'now': now(), 'post_list': post_list, 'category': category, 'popular_post': popular_post,
                   'trending_post': trending_post,})
def Life_Style(request):
    category = Category.objects.get(category='Life Style')
    post_list = Post.objects.filter(category=category).order_by('-date')
    popular_post = Post.objects.filter(rating='3').order_by('-date')[:5]
    trending_post = Post.objects.filter(rating='4').order_by('-date')[:5]
    return render(request, 'post/category_three.html',
                  {'now': now(), 'post_list': post_list, 'category': category, 'popular_post': popular_post,
                   'trending_post': trending_post,})

def Science_and_Environment(request):
    category = Category.objects.get(category='Science and Environment')
    post_list = Post.objects.filter(category=category).order_by('-date')
    popular_post = Post.objects.filter(rating='3').order_by('-date')[:5]
    trending_post = Post.objects.filter(rating='4').order_by('-date')[:5]
    return render(request, 'post/category_three.html',
                  {'now': now(), 'post_list': post_list, 'category': category, 'popular_post': popular_post,
                   'trending_post': trending_post,})

def post(request,slug):
    post = get_object_or_404(Post,slug=slug)
    share_string=quote_plus(post.title)
    return render(request, 'post/single_center.html',{'now':now(),'post':post,'share_string':share_string})


def create_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect(reverse('post:index'))
        else:
            form = PostForm
        return render(request,'post/post_form.html',{'form': form})
    else:
        return redirect(reverse('post:index'))




