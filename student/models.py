from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    cat=(('1',1),('2',2),('3',3),('4',4)
        ,('5',5),('6',6),('7',7),('8',8),('9',9),('10',10))
    sem=models.CharField(choices=cat,max_length=20)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/Student/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name