from django import forms

Carreras = [('Licenciatura en Matemática','Licenciatura en Matemática'), ('Licenciatura en Física','Licenciatura en Física')]

class formularioRegistro(forms.Form): # creacion del html, en base a 'signin.html'
    nickname = forms.CharField()
    email = forms.EmailField()
    carrera = forms.ChoiceField(choices = Carreras)
    CUI = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput, label = 'Contraseña')
    confPassword = forms.CharField(widget = forms.PasswordInput, label = 'Confirmar Contraseña')


class formularioLogin(forms.Form):
    nickname = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput, label = 'Contraseña')
