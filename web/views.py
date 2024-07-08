from .models import *
from django.shortcuts import render
from django.views.generic import ListView


def index(request):
    return render(request, 'under_construction.html')

class PortifolioListView(ListView):
    model = Portifolio
    template_name = 'index.html'
    context_object_name = 'portifolios'

    def get_queryset(self):
        return Portifolio.objects.select_related('image', 'category').all()
