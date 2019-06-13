from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Results
from import_export.admin import ImportExportModelAdmin


class ResultsAdmin(admin.ModelAdmin):
    list_display=('id','name','department','semister','roolno','marks','pass_fail')
    list_display_links=('id','name','roolno')
    list_per_page=10
    search_fields=('name','roolno')
    list_filter=('date_added',)

admin.site.register(Results,ResultsAdmin)
