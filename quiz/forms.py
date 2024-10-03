from django import forms
from django.contrib.auth.models import User
from . import models

# forms.py
from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(
        label='Upload CSV File',
        help_text='Select a CSV file containing questions for Exam.'
    )

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class TeacherSalaryForm(forms.Form):
    salary=forms.IntegerField()

class CourseForm(forms.ModelForm):
    class Meta:
        model=models.Course
        fields=['sem','course_name','question_number','total_marks']
        
from django import forms

class SemesterFilterForm(forms.Form):
    SEMESTER_CHOICES = [
        (1, 'Semester 1'),
        (2, 'Semester 2'),
        (3, 'Semester 3'),
        (4, 'Semester 4'),
        (5, 'Semester 5'),
        (6, 'Semester 6'),
        (7, 'Semester 7'),
        (8, 'Semester 8'),
        (9, 'Semester 9'),
        (10, 'Semester 10'),
        
        # Add more semester options up to 10 as needed
    ]
    
    sem = forms.ChoiceField(choices=SEMESTER_CHOICES, label='Select Semester')

class QuestionForm(forms.ModelForm):
    
    #this will show dropdown __str__ method course model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in course model and return it
    courseID=forms.ModelChoiceField(queryset=models.Course.objects.all(),empty_label="Course Name", to_field_name="id")
    class Meta:
        model=models.Question
        fields=['marks','question','option1','option2','option3','option4','answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 82})
        }
