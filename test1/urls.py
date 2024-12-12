from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('Student/', views.student_view, name='student'),
    path('Teacher/', views.Teacher_view, name='teacher'),
]
