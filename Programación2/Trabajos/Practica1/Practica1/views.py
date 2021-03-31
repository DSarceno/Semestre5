from django.http import HttpResponse


def saludo(request): # first view
    return HttpResponse("<html><body><h1>Hola HDPs</h1></body></html>")
