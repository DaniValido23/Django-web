from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy

from django.core.handlers.wsgi import WSGIRequest
from django.contrib.admin.views.decorators import staff_member_required

from .models import Service
from .forms import ServiceForm, OrderForm

from django.utils import timezone

class OrderSuccess(TemplateView):
    template_name = 'services/order_success.html'

class ServiceCreateOrder(CreateView):
    form_class = OrderForm
    template_name = 'services/client_order.html'
    success_url = reverse_lazy('services:order_success')

    def form_valid(self, form):
        new_order = form.save(commit=False)
        new_order.save()

        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ServiceCreateOrder, self).get_form_kwargs()
        kwargs['request'] = self.request

        return kwargs


def _create_dictionary(order_data: str):
    dictionary = {}

    products = order_data.split('|')

    for product in products:
        id, quantity = product.split('-')
        dictionary[int(id)] = float(quantity)

    return dictionary


def perform_order(request: WSGIRequest):
    order = list()

    if request.method == 'POST':
        order_data = request.POST['order_data']

        products = _create_dictionary(order_data)
        total = 0.0

        for p_id in products.keys():
            quantity = products[p_id]

            if quantity > 0:
                product_dictionary = {}
                service = Service.objects.get(pk=p_id)

                product_dictionary['title'] = service.title
                product_dictionary['subtitle'] = service.subtitle
                product_dictionary['quantity'] = quantity
                product_dictionary['price'] = 100.0
                product_dictionary['subtotal'] = quantity * 100.0

                total += (quantity * product_dictionary['price'])

                order.append(product_dictionary)

        request.session['total'] = float(total)
        request.session['order_detail'] = order

    return render(request, 'services/order_detail.html', {
        'order': order,
        'total': float(total)
    })


class ServiceListView(ListView):
    model = Service
    paginate_by = 1

class ServiceDetailView(DetailView):
    model = Service

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# @method_decorator(staff_member_required, name='dispatch')
class ServiceCreateView(CreateView):
    model = Service
    fields = [ 'title', 'subtitle', 'content', 'image' ]
    success_url = reverse_lazy('services:service_list')

class ServiceUpdateView(UpdateView):
    model = Service
    fields = [ 'title', 'subtitle', 'content', 'image' ]
    success_url = reverse_lazy('services:service_list')
    template_name_suffix = '_update'

@staff_member_required()
def delete(request: WSGIRequest, service_id: int):
    service = Service.objects.get(id=service_id)
    service.delete()

    return HttpResponseRedirect(reverse_lazy('services:service_list'))
