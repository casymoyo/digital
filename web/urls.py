from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('index/', PortifolioListView.as_view(), name='home'),
]