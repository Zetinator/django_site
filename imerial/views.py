from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.contrib import messages
from django.conf import settings

from django.core.mail import BadHeaderError, send_mail

from .forms import ContactForm
from .forms import SubscribeForm

# Create your views here.

# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'from@example.com',
#     ['to@example.com'],
#     fail_silently=False,
# )

# def cotizacion(request):
#     if request.method == 'POST': # If the form has been submitted...
#         form = ContactForm(request.POST) # A form bound to the POST data
#         if form.is_valid(): # All validation rules pass
#             # Process the data in form.cleaned_data
#             # ...
#
#             # print(form.cleaned_data['Name'])
#             print(form.cleaned_data['Name'])
#
#             return HttpResponseRedirect('/thanks/') # Redirect after POST
#     else:
#         form = ContactForm() # An unbound form
#
#     return HttpResponseRedirect('contact.html', {
#         'form': form,
#     })

# Create your views here.
def index(request):
    aux = 'Erick es genial'
    context = {'aux': aux}
    return render(request, 'imerial/index.html', context)

def servicios(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Servicio'

            name = form.cleaned_data['name']
            message = 'Nombre: ' + name + '\n'
            tel = form.cleaned_data['tel']
            message = message + 'Telefono: ' + tel + '\n'
            message = message + 'E-mail: ' + form.cleaned_data['email'] + '\n'
            from_email = settings.EMAIL_HOST_USER
            message = message + form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER], fail_silently = True)
            except BadHeaderError:
                messages.error(request, 'Revisa tus datos algo esta mal...')
            messages.success(request, 'Tu solicitud ha sido enviada! descuida te responderemos a la brevedad!')
    return render(request, 'imerial/servicios.html',  {'form': form})

def productos(request):
    aux = 'Erick es genial'
    context = {'aux': aux}
    return render(request, 'imerial/productos.html', context)

def detail_coccion(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Cotizacion'

            name = form.cleaned_data['name']
            message = 'Nombre: ' + name + '\n'
            tel = form.cleaned_data['tel']
            message = message + 'Telefono: ' + tel + '\n'
            message = message + 'E-mail: ' + form.cleaned_data['email'] + '\n'
            from_email = settings.EMAIL_HOST_USER
            message = message + form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER], fail_silently = True)
            except BadHeaderError:
                messages.error(request, 'Revisa tus datos algo esta mal...')
            messages.success(request, 'Tu solicitud ha sido enviada! descuida te responderemos a la brevedad!')
    return render(request, 'imerial/detail_coccion.html', {'form': form})

def detail_refrigeracion(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Cotizacion'

            name = form.cleaned_data['name']
            message = 'Nombre: ' + name + '\n'
            tel = form.cleaned_data['tel']
            message = message + 'Telefono: ' + tel + '\n'
            message = message + 'E-mail: ' + form.cleaned_data['email'] + '\n'
            from_email = settings.EMAIL_HOST_USER
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER], fail_silently = True)
            except BadHeaderError:
                messages.error(request, 'Revisa tus datos algo esta mal...')
            messages.success(request, 'Tu solicitud ha sido enviada! descuida te responderemos a la brevedad!')
    return render(request, 'imerial/detail_refrigeracion.html', {'form': form})

def detail_aceros(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Cotizacion'

            name = form.cleaned_data['name']
            message = 'Nombre: ' + name + '\n'
            tel = form.cleaned_data['tel']
            message = message + 'Telefono: ' + tel + '\n'
            message = message + 'E-mail: ' + form.cleaned_data['email'] + '\n'
            from_email = settings.EMAIL_HOST_USER
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER], fail_silently = True)
            except BadHeaderError:
                messages.error(request, 'Revisa tus datos algo esta mal...')
            messages.success(request, 'Tu solicitud ha sido enviada! descuida te responderemos a la brevedad!')
    return render(request, 'imerial/detail_aceros.html', {'form': form})

def detail_electricos(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Cotizacion'

            name = form.cleaned_data['name']
            message = 'Nombre: ' + name + '\n'
            tel = form.cleaned_data['tel']
            message = message + 'Telefono: ' + tel + '\n'
            message = message + 'E-mail: ' + form.cleaned_data['email'] + '\n'
            from_email = settings.EMAIL_HOST_USER
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER], fail_silently = True)
            except BadHeaderError:
                messages.error(request, 'Revisa tus datos algo esta mal...')
            messages.success(request, 'Tu solicitud ha sido enviada! descuida te responderemos a la brevedad!')
    return render(request, 'imerial/detail_electricos.html', {'form': form})
