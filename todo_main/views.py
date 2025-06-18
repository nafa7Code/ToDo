from multiprocessing import context
from django.shortcuts import render


def home(request):
    return render(request, 'todo/home.html', context)
