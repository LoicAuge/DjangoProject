from django.forms import DateInput
from django.forms.models import ModelForm
from .models import Student, Cursus, Presence

class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ("first_name", "last_name", "birth_date", "email", "phone", "comments", "cursus")

class CursusForm(ModelForm):

    class Meta:
        model = Cursus
        fields = ("name", "year_from_bac", "scholar_year")

class PresenceForm(ModelForm):

    class Meta:
        model = Presence
        fields = ("date_presence", "isMissing", "reason", "student")
