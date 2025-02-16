
from django.shortcuts import render
from .models import *
def index(request):
    student=Student.objects.all()
    kurs=Kurs.objects.all()
    context= {
        "student": student,
        "kurs": kurs,
        "title": "News Title"

    }
    return render(request,'student/index.html',context=context)