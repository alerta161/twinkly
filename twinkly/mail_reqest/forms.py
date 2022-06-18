from django import forms

class ContactForm(forms.Form):
    imie = forms.EmailField(label='imię', required=True)
    surname = forms.CharField(label='Nazwisko', required=True)
    mail = forms.CharField(label='E-mail', widget=forms.Textarea, required=True)
    telefon = forms.CharField(label='Telefon', widget=forms.Textarea, required=True)
    message = forms.CharField(label='Wiadomość', widget=forms.Textarea, required=True)
