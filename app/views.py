from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from app.models import Students, Teacher
from django.db.models import Q
from app.serializers import GetTeachersSerializer

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

    # Run some ORM Queries

    # Henry	18	Coding	True	Sept. 28, 2025
	# Mikel	33	Science	False	Sept. 28, 2025
	# John	23	Coding	True	Sept. 28, 2025
	# Omar	8	Coding	False	Sept. 28, 2025
	# Ahmed	50	Math	True	Sept. 28, 2025
	# Khalid	40	History	True	Sept. 28, 2025

    # 1 - Fetch all coding teachers
    coding_teacher = Teacher.objects.filter(subject="Coding")
    # print(coding_teacher)

    # 2 - Fetch all non active teachers
    non_active_teachers = Teacher.objects.filter(is_active=False)
    # print(non_active_teachers)

    # 3 - Fetch teachers that are 30 years old or above
    old_teachers = Teacher.objects.exclude(age__lt=30)
    # print(old_teachers)

    # 4 - Fetch active coding teachers that are 20 years old or above
    young_teachers = Teacher.objects.filter(
        is_active=True,
        subject="Coding",
        age__gte=20
    )
    # print(young_teachers)

    # 5 - Fetch all that are aged between 20 and 50
    teachers_between_20_and_50 = Teacher.objects.filter(
        age__gte=20,
        age__lte=50
        )
    # print(teachers_between_20_and_50
    # ----------------------------------------------------------------------------
    # -  OR conditions with Q objects
    # from django.db.models import Q
    # junior_or_named_ali = TeamMember.objects.filter(Q(age__lt=18) | Q(name__icontains="ali"))
    # active_and_title_set = TeamMember.objects.filter(Q(is_active=True) & Q(title__isnull=False))

    # 6 - Fetch all teachers that are either Coding or age greater than 30
    coding_or_above_30_age_teachers = Teacher.objects.filter(
        Q(subject="Coding") | Q(age__gte=30)
    )
    # print(coding_or_above_30_age_teachers)

    # 7 - Fetch all teachers that are either Coding or History
    # subject__in=["Coding", "History"]
    coding_or_history_teachers = Teacher.objects.filter(
        subject__in=["Coding", "History"]
    )
    print(coding_or_history_teachers)


    # 8 - Fetch all teachers that their name includes the letter 'o' __icontains
    teachers_contain_o = Teacher.objects.filter(name__icontains="O")
    print(teachers_contain_o)


    # 9 - Fetch all teachers having them sorted by age from oldest to youngest
    # ----------------------------------------------------------------------------
    # - ) ORDERING results
    # by_age_asc = TeamMember.objects.all().order_by("age") # ascending # from the smallest to the largest
    # by_age_desc = TeamMember.objects.order_by("-age") # descending # from the largest to the smallest

    oldest_to_youngest_teachers = Teacher.objects.order_by("-age")
    # for teacher in oldest_to_youngest_teachers:
    #     print(f"Name - {teacher.name}, Age - {teacher.age}")


    # 10 - Fetch all teachers having them sorted by is_active (True show first) and then as 2nd level sorting by age descending
    # by_multiple = TeamMember.objects.order_by("-is_active", "name")
    by_multiple_teachers = Teacher.objects.order_by("-is_active", "-age")
    # for teacher in by_multiple_teachers:
    #     print(f"Name - {teacher.name}, Age - {teacher.age}, IsActive - {teacher.is_active}")

    # 11 - Fetch active Coding teachers having them sorted by  name descending
    active_coding_teacher_by_name_desc = Teacher.objects.filter(
        Q(is_active=True) & Q(subject="Coding")
    ).order_by("-name")
    # for teacher in active_coding_teacher_by_name_desc:
    #     print(f"Name - {teacher.name}, Subject - {teacher.subject}, IsActive - {teacher.is_active}")

    # 12 - Fetch all Coding teachers sorted by name ascending (get first 2)
    # ----------------------------------------------------------------------------
    # - LIMIT and OFFSET (use slicing)
    # first_five = TeamMember.objects.all()[:5]
    # next_five = TeamMember.objects.all()[5:10]
    # youngest_three = TeamMember.objects.order_by("age")[:3]
    teacher_asc_first_2 = Teacher.objects.filter(subject="Coding").order_by("name")[:2]
    # for teacher in teacher_asc_first_2:
    #     print(f"Name - {teacher.name}, Subject - {teacher.subject}, IsActive - {teacher.is_active}")


    # 13 - Fetch count of all members
    # ----------------------------------------------------------------------------
    # - COUNTS
    # total_members = TeamMember.objects.count()
    # count() returns Int value
    coding_count = Teacher.objects.filter(subject="Coding").count() # -> 3
    # print(coding_count)

    # 14 - Check if Ahmad exists on all teachers
    # # has_any_cards = Card.objects.exists()
    # exists() returns either True/False
    is_ahmad_exists = Teacher.objects.filter(name="Ahmed").exists()
    print(f"\nis_ahmad_exists : {is_ahmad_exists}")

    # 15 - Lookup examples:
    # ----------------------------------------------------------------------------
    # 10) FIELD LOOKUPS (more examples)
    # name_starts_with_a = TeamMember.objects.filter(name__istartswith="a")
    # name_ends_with_n = TeamMember.objects.filter(name__iendswith="n")
    # age_between = TeamMember.objects.filter(age__range=(18, 30))
    # name_in_list = TeamMember.objects.filter(name__in=["Ali", "Mona", "John"])
    # description_has_sunset = Card.objects.filter(description__icontains="sunset")


    # 16 -  PICK specific columns as list of actual dicts
    # limit_columns_as_list_of_actual_dicts = TeamMember.objects.values("name", "age")  # list of dicts
    all_teachers = Teacher.objects.all().values("name", "subject")
    # all_teachers eg: <QuerySet [{'name': 'Khalid', 'subject': 'History'}, {'name': 'Ahmed', 'subject': 'Math'}, {'name': 'Omar', 'subject': 'Coding'}, {'name': 'John', 'subject': 'Coding'}, {'name': 'Mikel', 'subject': 'Science'}, {'name': 'Henry', 'subject': 'Coding'}]>
    # all(): SELECT * FROM teachers
    # all().values("name", "subject"): SELECT name, subject FROM teachers
    # print(f"all_teachers : {all_teachers}")
    # for teacher in all_teachers:
    #     print(f"Name - {teacher['name']}, Subject - {teacher['subject']}")
        # if try to access , IsActive - {teacher.is_active} = it will return error

    # 17 - PICK specific columns as QuerySet
    all_teachers = Teacher.objects.all().only("name", "subject")
    # print(f"all_teachers : {all_teachers}")
    # all(): SELECT * FROM teachers
    # all().only("name", "subject"): SELECT name, subject FROM teachers
    # for teacher in all_teachers:
    #     print(f"Name - {teacher.name}, Subject - {teacher.subject}, IsActive - {teacher.is_active}")
    #     # if try to access , IsActive - {teacher.is_active} = it will not error


    # 18 - Fetch all names from teachers as python list
    # values_list() accepts only single column
    just_names = list(Teacher.objects.values_list("name", flat=True))  # list of names
    print(f"just_names : {just_names}") # ['Khalid', 'Ahmed', 'Omar', 'John', 'Mikel', 'Henry']

    context = {
        "teachers": teachers
    }

    return render(request, "app/bootstrap-home.html", context)


@api_view(['GET'])
def get_teachers(request):
    all_teachers = Teacher.objects.all()
    serializer = GetTeachersSerializer(all_teachers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_teacher(request):
    Teacher.objects.create(
        name=request.data.get("name"),
        age=request.data.get("age"),
        subject=request.data.get("subject"),
    )

    return Response({})


@api_view(['DELETE'])
def delete_teacher(request, teacher_id):
    # get(id = teacher_id) this will raise DoesNotExists error, in case there is not teacher with the given id.
    teacher = Teacher.objects.get(id = teacher_id)#.delete()
    teacher.delete()
    return Response({})


@api_view(['PUT'])
def update_teacher(request, teacher_id):
    # get(id = teacher_id) this will raise DoesNotExists error, in case there is not teacher with the given id.
    teacher = Teacher.objects.get(id = teacher_id)
    teacher.name = request.data.get("name")
    teacher.age = request.data.get("age")
    teacher.subject = request.data.get("subject")
    teacher.save()
    return Response({})
