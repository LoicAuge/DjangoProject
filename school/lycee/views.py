from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from .models import Cursus, Student, Presence, Appel
from .forms import StudentForm, CursusForm, PresenceForm
from django.template import loader
from django.views.decorators.csrf import csrf_protect

def index(request):
    result_list = Cursus.objects.order_by('name')
    context = {'liste': result_list}
    return render(request, 'lycee/index.html', context)

def detail(request, idC):
    result_list = Student.objects.filter(cursus_id = idC)
    cursus = Cursus.objects.get(id=idC)
    context = {'liste': result_list, 'cursusName': cursus.name, 'cursusID': cursus.pk}
    return render(request, 'lycee/cursus/list-onCursus.html', context)

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
    template_name = "lycee/student/modify.html"

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
    template_name = "lycee/cursus/modify_cursus.html"

    def get_success_url(self):
        return reverse("detail", args=(self.object.pk,))

class PresenceCreateView(CreateView):
    model = Presence
    form_class = PresenceForm
    template_name = "lycee/presence/create_presence.html"

    def get_success_url(self):
        return reverse("index")

def cursusCall(request, idC):
    if request.method == 'POST':
        stud_list = Student.objects.filter(cursus_id=idC)
        cursuse = Cursus.objects.get(id=idC)
        app = Appel(date=request.POST.get("date_appel",""), cursus= cursuse)
        app.save()
        for stud in stud_list:
            if request.POST.get(str(stud.id),"") == 'on':
                boolTemp = True
            else:
                boolTemp = False
            pres = Presence(date_presence=request.POST.get("date_appel",""), student=stud, appel=app, isMissing=boolTemp)
            pres.save()
        return redirect("index")
    else:
        stud_list = Student.objects.filter(cursus_id=idC)
        cursus = Cursus.objects.get(id=idC)
        context = {'liste': stud_list, 'cursus': cursus}
        return render(request, 'lycee/appel/cursusCall.html', context)

def detailAppel(request):
    result_list = Appel.objects.order_by('date')
    resList = []
    for appel in result_list:
        templist = []
        cursus = Cursus.objects.get(id=appel.cursus.id)
        templist.append(appel.id)
        templist.append(appel.date)
        templist.append(cursus.name)
        resList.append(templist)
    context = {'liste': resList}
    return render(request, 'lycee/appel/list-appel.html', context)