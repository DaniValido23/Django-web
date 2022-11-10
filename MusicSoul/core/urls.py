from django.urls import path

from django.contrib.auth import views as auth_views

from core import views

core_urlpatterns = (
    [
        path('', views.HomeView.as_view(), name='home'),
        path('about/', views.about, name='about'),
        path('store/', views.store, name='store'),
        path('policy/', views.policy, name='policy'),
        # path('contact/', views.contact, name='contact'),
        # path('blog/', views.blog, name='blog'),
        # path('services/', views.services, name='services'),

        # Logout url
        path('logout/', auth_views.LogoutView.as_view(), name='logout')
    ],
    'core'
)
