from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        surname = request.POST['surname']
        mail = request.POST['mail']
        telefon = request.POST['telefon']
        content = request.POST['content']

        send_mail(
            f'{user_name}{surname}',
            f'Телефон:{telefon}\n'
            f'Почта:{mail}\n'
            f'Сообщение:{content}',
            'sashaalerta@gmail.com', #почта отправляющая
            ["hubichaleksandr@gmail.com"] #почта принимающая
        )

        return render(request, 'mail_reqest/new_base.html',
                      {'user_name': user_name, "surname": surname, "mail": mail, "telefon": telefon,
                       "content": content})
    else:
        return render(request, 'mail_reqest/new_base.html', {})
