from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from .models import Cursus, Student
from .forms import StudentForm
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

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "lycee/student/create.html"

    def get_success_url(self):
        return reverse("detail_student", args=(self.object.pk,))

def detail_Student(request, idS):
    student = Student.objects.get(id = idS)
    context = {'eleve': student}
    return render(request, 'lycee/student/detail_eleve.html', context)

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "lycee/student/create.html"

    def get_success_url(self):
        return reverse("detail_student", args=(self.object.pk,))