from django.urls import path

from blog import views

blog_urlpatterns = (
    [
        path('', views.blog, name='blog'),
        path('category/<int:category_id>', views.categories, name='category')
    ],
    'blog'
)
