from django.shortcuts import render

# Create your views here.
from app.models import Students, Teacher

def home(request):
    # ORM : Object Relational Mapping
    # ORM Query : Students.objects.all()
    # SQL Query : SELECT * FROM app_students
    students = Students.objects.all()
    # print(f"\n\nstudents : {students}\n\n")
    # print(f"\n\nstudents type : {type(students)}\n\n")


    # students = [
    #     {
    #         "id": 1,
    #         "name": "Adam",
    #         "age": 10,
    #     },
    #     {
    #         "id": 1,
    #         "name": "Jane",
    #         "age": 15,
    #     },
    #     {
    #         "id": 1,
    #         "name": "Mike",
    #         "age": 20,
    #     }
    # ]


    # for student in students:
    #     # Printing our testing Dict. : print(f"Name: {student['name']} | Age : {student['age']}")
    #     # Printing our QuerySet:
    #     print(f"Name: {student.name} | Age : {student.age}")

    # context is a common naming for the dict that django sends to the html file
    # this dict will contains all the data that html page shall uses.
    context = {
        "title": "Our Students:",
        "students": students,
    }

    return render(request, "app/home.html", context)


def bootstrap_home(request):

    teachers = Teacher.objects.all()

    context = {
        "teachers": teachers
    }

    return render(request, "app/bootstrap-home.html", context)