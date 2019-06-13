from django.urls import path
from . import views

urlpatterns = [
    path('add_student/',views.add_student.as_view(),name="add_student"),
    path('view_student/<int:pk>',views.view_student.as_view(),name='view_student'),
    path('delete_student/<int:pk>',views.delete_student,name='delete_student'),
    path('view_student_detail/<int:pk>',views.view_student_detail.as_view(),name='view_student_detail'),
    path('student_login/',views.student_login,name='student_login'),
    path('student_home/',views.student_home,name='student_home'),
    path('view_student_profile/',views.view_student_profile,name='view_student_profile'),
    path('view/',views.view,name='view'),
    path('feepayment/',views.feepayment,name='feepayment'),
    path('view_department_students/<int:pk>',views.view_department_students,name='view_department_students'),
]