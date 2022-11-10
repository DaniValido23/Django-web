from django.urls import path

from services import views

services_urlpatterns = (
    [
        path('', views.ServiceListView.as_view(), name='service_list'),
        path('create', views.ServiceCreateView.as_view(), name='create'),
        path('update/<pk>', views.ServiceUpdateView.as_view(), name='update'),
        path('delete/<int:service_id>', views.delete, name='delete'),

        path('detail/<pk>', views.ServiceDetailView.as_view(), name='service_detail'),

        path('order_detail', views.perform_order, name='order_detail'),
        path('order_success', views.OrderSuccess.as_view(), name='order_success'),
        path('create_order', views.ServiceCreateOrder.as_view(), name='create_order'),
    ],
    'services'
)
