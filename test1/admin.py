from django.contrib import admin
from .models import Teacher, Student
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject')
    list_filter = ('last_name', 'subject')
    search_fields = ('last_name', 'subject')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'teacher')
    list_filter = ('last_name', 'teacher')
    search_fields = ('last_name', 'teacher')

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)