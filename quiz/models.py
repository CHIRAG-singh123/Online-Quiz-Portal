from django.db import models

from student.models import Student
class Course(models.Model):
   cat=(('1',1),('2',2),('3',3),('4',4)
        ,('5',5),('6',6),('7',7),('8',8),('9',9),('10',10))
   sem=models.ImageField(choices=cat)
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   def __str__(self):
        return self.course_name
   
class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

