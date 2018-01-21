from django import forms
from student.models import Student
from create.models import create_assignment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['date']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Divaker Soni','class': 'form-control'}),
            'roll_no': forms.TextInput(attrs={'class': 'form-control'}),
            'assignment': forms.Select(attrs={'class': 'form-control'}),
            'agn_file': forms.FileInput(attrs={'class': 'form-control'}),
        }

class create_assignmentForm(forms.ModelForm):
    class Meta:
        model = create_assignment
        exclude = ['date']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Divaker Soni','class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'deadline': forms.FileInput(attrs={'class': 'form-control'}),
        }