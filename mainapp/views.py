from django.views.generic import ListView
from django.shortcuts import render
from .models import *
# Create your views here

class ImageS(ListView):
    model = Notebook
    template_name = 'base.html'
    context_object_name = 'product'

def test_view(request):
    return(request,'base.html')
