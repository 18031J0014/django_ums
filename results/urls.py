from django.urls import path
from .import views
urlpatterns = [
    path('results/',views.results,name='results'),
    path('add_marks/',views.add_marks.as_view(),name='add_marks'),
]
