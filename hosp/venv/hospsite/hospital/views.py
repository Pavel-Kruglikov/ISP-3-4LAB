from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'hospital/index.html')


def about(request):
    return render(request, 'hospital/about.html')


def departments(request, depict):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Отделения больницы</h1><p>{depict}</p>")


def archive(request, year):
    if int(year) > 2019:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам лечения пациентов</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
