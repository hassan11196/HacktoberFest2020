from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    sem = models.CharField(max_length=20)

class teacher(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)



class BSCS(models.Model):
   class_schedule = models.CharField(max_length=200,null=True)
   course_work = models.CharField(max_length=200,null=True)
   sem = models.CharField(max_length=10,null=True)
   subject_teacher = models.CharField(max_length=200,null=True)
   
   def __str__(self):
      return self.course_work

class announcments(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
   msg = models.CharField(max_length=200, null=True)
   date = models.DateField(null=True)
   
   def __str__(self):
      return self.msg

class posts(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
   title_name = models.CharField(max_length=200,null=True)
   post_content = models.CharField(max_length=25000, null=True)

   def __str__(self):
      return self.title_name
