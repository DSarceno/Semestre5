from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.models import usuarios # tabla en base de datos
from users.forms import formularioRegistro, formularioLogin # formulario para crear html
from django.core.mail import send_mail # envio de correos
from django.conf import settings # datos para el envio de correos

# Create your views here.

encabezado = '<!DOCTYPE html> \n \
<html lang="es" dir="ltr"> \n \
  <head> \n \
    <meta charset="utf-8"> \n \
    <title>{name}</title> \n \
  </head> \n \
  <body> \n \
    <div style="text-align:center"> \n \
    <h1>Ingresar</h1> \n \
    <h5>Datos Personales</h5> \n \
    <form action='' method="POST">{% csrf_token %} \n \
        <table style="margin: 0 auto;"> \n \
            {{form.as_table}} \n \
        </table> \n \
        <input type = "submit" value = "Login"> \n \
    </form> \n \
    </div> \n \
  </body> \n \
</html>'



def registro(request):
    if request.method == 'POST':
        formulario = formularioRegistro(request.POST)
        if formulario.is_valid(): # validar la informacion ingresada en el formulario
            infFormulario = formulario.cleaned_data # crear un diccionario con dicha informacion

            if email_existence(infFormulario) or nickname_existence(infFormulario): # si ya existen
                return render(request, 'registro.html',{'form':formulario}) # regreso a la pagina de registro
            elif (infFormulario['password'] == infFormulario['confPassword']):
                # ingreso de datos en base de datos
                #user = usuarios(email = infFormulario['email'], nickname = infFormulario['nickname'],CUI = infFormulario['CUI'], carrera = infFormulario['carrera'], password = infFormulario['password'])
                #user.save() # guardado
                print('Ok')
                # Envío de confirmacion de registro (PROBLEMAS CON GMAIL)
                ### send_mail('Registro','Su registro ha sido aprobado correctamente.', 'dsarceno69@gmail.com',[infFormulario['email']],fail_silently = False,)
                return redirect('/login/') # corroboracion de ingreso correcto
            else:
                return render(request, 'registro.html',{'form':formulario}) # regreso a la pagina de registro

    else:
        formulario = formularioRegistro()
    return render(request, 'registro.html',{'form':formulario}) # al ingresar al servidor, lleva a la pagina de registro

# Funciones ayuda
def email_existence(dict): # false si no existe ningun email igual en la base de datos
    y_n = True
    try:
        usuarios.objects.get(email = dict['email'])
    except usuarios.MultipleObjectsReturned:
        return y_n
    except usuarios.DoesNotExist:
        y_n = False
        return y_n
    return y_n


def nickname_existence(dict): # false si no existe ningun usuario con el mismo nickname
    y_n = True
    try:
        usuarios.objects.get(nickname = dict['nickname'])
    except usuarios.MultipleObjectsReturned:
        return y_n
    except usuarios.DoesNotExist:
        y_n = False
        return y_n
    return y_n

def password_existence(dict): # Como es poco probable que existan contraseñas iguales, se validará de esta forma
    y_n = True
    try:
        usuarios.objects.get(password = dict['password'])
    except usuarios.MultipleObjectsReturned:
        return y_n
    except usuarios.DoesNotExist:
        y_n = False
        return y_n
    return y_n


def login(request):
    if request.method == 'POST':
        formulario = formularioLogin(request.POST)
        if formulario.is_valid(): # validar la informacion ingresada en el formulario
            infFormulario = formulario.cleaned_data # crear un diccionario con dicha informacion
            print(email_existence(infFormulario), nickname_existence(infFormulario), password_existence(infFormulario))
            if email_existence(infFormulario) and nickname_existence(infFormulario) and password_existence(infFormulario): # si ya existen
                return render(request, 'gracias.html') # aceptacion del ingreso
            else:
                return render(request, 'ingreso.html',{'form':formulario}) # regreso a la pagina de ingreso

    else:
        formulario = formularioLogin()
    return render(request, 'ingreso.html',{'form':formulario}) # al ingresar al servidor, lleva a la pagina de ingreso
