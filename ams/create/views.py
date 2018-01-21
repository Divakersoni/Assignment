from django.shortcuts import render
from student.models import Student
from student.forms import StudentForm
from django.http import HttpResponseRedirect
from django.utils import timezone

def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            abc = form.save(commit=False)
            if timezone.now().date() <= abc.assignment.deadline:
                form.save()
                return HttpResponseRedirect('/thankyou/')
            else:
                return HttpResponseRedirect('/sorry/')
    else:
        form = StudentForm()
    return render(request,'index.html',{'form':form})

def thankyou(request):
    return render(request,'index2.html')

def sorry(request):
    return render(request,'index3.html')

def index4(request):
    S = Student.objects.all()
    return render(request,'index4.html',{'S':S,})