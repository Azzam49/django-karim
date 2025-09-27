from django.shortcuts import render

# Create your views here.
from app.models import Students

def home(request):
    # ORM : Object Relational Mapping
    # ORM Query : Students.objects.all()
    # SQL Query : SELECT * FROM app_students
    students = Students.objects.all()

    print(f"\n\nstudents : {students}\n\n")
    print(f"\n\nstudents type : {type(students)}\n\n")

    return render(request, "app/home.html", {})