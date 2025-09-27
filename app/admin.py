from django.contrib import admin

# Register your models here.
from app.models import Students

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    pass