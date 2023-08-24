from django.http import HttpResponse

def products(request, id=0):
    return HttpResponse(f"Список товаров {id}")

def new(request, id=0):
    return HttpResponse(f"Новые товары {id}")

def top(request, id=0):
    return HttpResponse(f"Популярные товары {id}")

def user_get(request):
    name = request.GET.get("name", "Nemo")
    age = request.GET.get("age", 0)
    return HttpResponse(f"<h2>Имя: {name}; Возраст: {age}</h2>")

def user(request, name):
    return HttpResponse(f"<h2>Имя: {name}</h2>")

def user2(request, name="Nemo", age=0):
    return HttpResponse(f"<h2>Имя: {name}; Возраст: {age}</h2>")

def user3(request, name="Nemo", age=0):
    return HttpResponse(f"<h2>Имя: {name}; Возраст: {age}</h2>")

def zag(request):
    return HttpResponse("HEllo All!", headers={"SecretCode": "2123543"})

def zag_2(request):
    return HttpResponse("ErroR occured", status=400, reason="Incorrect data")

def zag_3(request):
    return HttpResponse("<h1> Plain text </h1>", content_type="text/plain", charset="utf-8")

def index(request):
    host = request.META["HTTP_HOST"] # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"] # данные браузера
    path = request.path # запрошеный путь
    return HttpResponse(f"""
                        <h2> О запросе </h2>
                        <p>Хост: {host} </p>
                        <p>Браузер {user_agent}</p>
                        <p>Путь {path}</p>
                        """)


def about(request, name, age):
    return HttpResponse(f"""
                        <h2> О пользователе </h2>
                        <p>Имя: {name} </p>
                        <p>Возраст {age}</p>
                        """)


def contact(request):
    return HttpResponse("Контакты")
