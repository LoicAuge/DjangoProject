from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cursus, Student
from django.template import loader

def index(request):
    result_list = Cursus.objects.order_by('name')
    context = {'liste': result_list}
    return render(request, 'lycee/index.html', context)

def detail(request, idC):
    result_list = Student.objects.filter(cursus_id = idC)
    cursus = Cursus.objects.get(id=idC)
    context = {'liste': result_list, 'cursusName': cursus.name}
    return render(request, 'lycee/list-onCursus.html', context)