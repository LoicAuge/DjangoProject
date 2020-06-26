from django.contrib import admin

# Register your models here.
from .models import Student, Cursus

class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone")


admin.site.register(Student, StudentAdmin)
admin.site.register(Cursus)
