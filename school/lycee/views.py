from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from .models import Cursus, Student, Presence
from .forms import StudentForm, CursusForm, PresenceForm
from django.template import loader

def index(request):
    result_list = Cursus.objects.order_by('name')
    context = {'liste': result_list}
    return render(request, 'lycee/index.html', context)

def detail(request, idC):
    result_list = Student.objects.filter(cursus_id = idC)
    cursus = Cursus.objects.get(id=idC)
    context = {'liste': result_list, 'cursusName': cursus.name, 'cursusID': cursus.pk}
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

class CursusCreateView(CreateView):
    model = Cursus
    form_class = CursusForm
    template_name = "lycee/cursus/create_cursus.html"

    def get_success_url(self):
        return reverse("detail", args=(self.object.pk,))

class CursusUpdateView(UpdateView):
    model = Cursus
    form_class = CursusForm
    template_name = "lycee/cursus/create_cursus.html"

    def get_success_url(self):
        return reverse("detail", args=(self.object.pk,))

class PresenceCreateView(CreateView):
    model = Presence
    form_class = PresenceForm
    template_name = "lycee/create_presence.html"

    def get_success_url(self):
        return reverse("index")