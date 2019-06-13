from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('admin_home/',views.admin_home,name="admin_home"),
] 