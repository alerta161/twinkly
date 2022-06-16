from django.shortcuts import render


# Create your views here
def index(request):
    return render(request, 'mail_reqest/new_base.html')
