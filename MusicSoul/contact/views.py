import time

from django.shortcuts import render

from django.http import HttpResponseRedirect, JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse_lazy

from .forms import ContactForm

from blog.models import Category

def executeAJAX(request: WSGIRequest):
    if request.method == 'POST':
        option = request.POST.get('value', '')

        response = {}
        options = {}

        if option == '1':
            response['status'] = 'Ok'

            for category in Category.objects.all():
                options[category.id] = category.name

        elif option == '2':
            response['status'] = 'Ok'
            options['1'] = '2 - Option 1'
            options['2'] = '2 - Option 2'
            options['3'] = '2 - Option 3'

        else:
            response['status'] = 'Invalid'

        response['options'] = options

        # time.sleep(3)

        return JsonResponse(response)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print(f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}")

            email = form.cleaned_data['email']

            domain = email[email.find('@') + 1:]

            if domain != 'gmail.com':
                form.add_error('email', 'Email inválido')
                form.add_error('email', 'Únicamente correos de gmail están permitidos')

                return render(request, 'contact/contact.html', {
                    'form': form
                })

            return HttpResponseRedirect(reverse_lazy('contact:thanks'))

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': form
    })

def thanks(request):
    return render(request, 'contact/thanks.html')
