from django.shortcuts import render
from .models import Teacher, Student
# Create your views here.

def index(request):
    return render(request, 'test1/index.html')
  
def student_view(request):
    teacher_list = Teacher.objects.all()
    return render(request, 'test1/student.html',{
      'teacher_list': teacher_list,
    })
  
def Teacher_view(request):
    student_list = Student.objects.all()
    return render(request, 'test1/teacher.html',{
      'student_list': student_list,
    })
  