from django.shortcuts import render

from .models import Category, Post

def blog(request):
    posts = Post.objects.all()

    return render(request, 'blog/blog_list.html', {
        'posts': posts
    })

def categories(request, category_id):
    category = Category.objects.get(id=category_id)

    return render(request, 'blog/category.html', {
        'category': category
    })
