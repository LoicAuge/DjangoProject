from django.forms.models import ModelForm
from .models import Student, Cursus

class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ("first_name", "last_name", "birth_date", "email", "phone", "comments", "cursus")

class CursusForm(ModelForm):

    class Meta:
        model = Cursus
        fields = ("name", "year_from_bac", "scholar_year")