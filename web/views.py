from django.shortcuts import render


def index(request):
    return render(request, 'under_construction.html')

def home(request):
    return render(request, 'index.html')
