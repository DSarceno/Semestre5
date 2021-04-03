from django.shortcuts import render
from django.http import HttpResponse
from usersManagement.models import Users

# Create your views here.

def registro(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Nombre = request.POST['Nombre']
        Apellido = request.POST['Apellido']
        Contra = request.POST['Password']
        ConfContra = request.POST['ConfirmPassword']

        if (Contra == ConfContra) and (Users.objects.filter(nombre__icontains = Email) == []):
            user = Users(email = Email, nombre = Nombre, apellido = Apellido, password = Contra)
            user.save()


            return render(request, 'gracias.html')
    return render(request, 'signin.html')

def registrado(request):
    mensaje = 'Te has registrado exitosamente!'
    return HttpResponse(mensaje)
