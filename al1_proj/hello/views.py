from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello blin! </br> Главная..")


def about(request):
    return HttpResponse("О сайте")


def contact(response):
    return HttpResponse("Контакты")
