from django.shortcuts import render
from django.http import HttpResponse
from usersManagement.models import usuarios

# Create your views here.

def registro(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Nombre = request.POST['Nombre']
        Apellido = request.POST['Apellido']
        Nickname = request.POST['Nickname']
        Sexo = request.POST['sexo']
        Carrera = request.POST['Carrera']
        Contra = request.POST['Password']
        ConfContra = request.POST['ConfirmPassword']

        print(Email)
        print(Nickname)
        print(Sexo)
        print(Carrera)
        print(Contra)
        if (Contra != ConfContra):
            return render(request, 'signin.html')
        else:
            if ((usuarios.objects.filter(email__icontains = Email) != []) or (usuarios.objects.filter(nickname__icontains = Nickname) != [])):
                return render(request, 'signin.html')
            else:
                user = usuarios(email = Email, nickname = Nickname, nombre = Nombre, apellido = Apellido, sexo = Sexo, carrera = Carrera, password = Contra)
                user.save()
                return render(request, 'gracias.html')
    return render(request, 'signin.html')

def registrado(request):
    mensaje = 'Te has registrado exitosamente!'
    return HttpResponse(mensaje)
