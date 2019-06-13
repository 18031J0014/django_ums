from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Student
from import_export.admin import ImportExportModelAdmin


class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','gender','email','rollno','phone','department')
    list_display_links=('id','name')
    list_editable=('email',)
    list_per_page=10
    search_fields=('name','email','rollno','phone')
    list_filter=('gender','date_added',)

admin.site.register(Student,StudentAdmin)
