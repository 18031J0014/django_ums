from django.urls import path
from . import views

urlpatterns = [
   path('add_lecturer/',views.add_lecturer.as_view(),name='add_lecturer'),
   path('view_lecturer/',views.view_lecturer.as_view(),name='view_lecturer'),
   # path('view_lecturer/',views.view_lecturer,name='view_lecturer')
   path('view_lecturer_detail/<int:pk>',views.view_lecturer_detail.as_view(),name='view_lecturer_detail'),
   path('delete_lecturer/<int:pk>',views.delete_lecturer.as_view(),name='delete_lecturer'),
   path('lecturer_login/',views.lecturer_login,name='lecturer_login'),
   path('update_lecturer/<int:pk>',views.update_lecturer.as_view(),name='update_lecturer'),
   path('lecturer_home/',views.lecturer_home,name='lecturer_home'),
   path('update/',views.update,name="update"),
   path('view_lecturer_profile/',views.view_lecturer_profile,name='view_lecturer_profile'),


]
