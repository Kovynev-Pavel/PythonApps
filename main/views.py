from django.shortcuts import render
from django.http import HttpResponse

def pon(request):
    return render(request, 'main/index.html', {'Title': 'Главная'})


def otl(request):
    return render(request, 'main/we.html')


