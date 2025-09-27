from django.contrib import admin

# Register your models here.
from app.models import Students, Teacher

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass