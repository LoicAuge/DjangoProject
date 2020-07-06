from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cursus
from django.template import loader

def index(request):
    result_list = Cursus.objects.order_by('name')
    context = {'liste': result_list}
    return render(request, 'lycee/index.html', context)

def detail(request, id):
    resp = "resultat pour cursus {}".format(id)
    return HttpResponse(resp)