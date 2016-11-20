from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Student
from .forms import StudentForm

def home(request):
    now = datetime.datetime.now()
    students = Student.objects.all()
    output = ''
    for student in students:
        output += student.first_name + ' ' + student.last_name + ' '

    html = "<html><body><h1>Zekelabs</h1>Students now %s</body></html" %output
    return HttpResponse(html)

def about(request):
    print request.user
    html = "<html><body><h2>About Us</h2></body></html>"
    return HttpResponse(html)

def index(request):
    students = Student.objects.all()
    return render(request,'home.html',{'students':students, 'name':'awantik', 'info':{1:'a', 2:'b', 3:'c'}})

def info(request):
    form = StudentForm()
    return render(request,'form.html',locals())

def submit(request):
    f = StudentForm(request.POST)
    f.save()
    return HttpResponse('<html><body><h1>Thanks</h1></body></html>')


