from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)

    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
      
    def __str__(self):
        return self.full_name()
    
    

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)

 
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
      
    def __str__(self):
        return self.full_name()
    
