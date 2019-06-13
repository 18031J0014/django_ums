from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Lecturer
from import_export.admin import ImportExportModelAdmin


class LecturerAdmin(admin.ModelAdmin):
    list_display=('id','name','gender','email','info','phone','department')
    list_display_links=('id','name')
    list_editable=('info',)
    list_per_page=10
    search_fields=('name','email','info','phone')
    list_filter=('gender','date_added',)

admin.site.register(Lecturer,LecturerAdmin)
admin.site.unregister(Group)