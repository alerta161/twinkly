from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from twinkly.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


# Create your views here
def index(request):
    return render(request, 'mail_reqest/new_base.html')


def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            imie = form.cleaned_data['imię']
            surname = form.cleaned_data['Nazwisko']
            mail = form.cleaned_data['E-mail']
            telefon = form.cleaned_data['Telefon']
            try:
                send_mail(f'{imie}{surname} от {mail}', telefon, message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "new_base.html", {'form': form})


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')
