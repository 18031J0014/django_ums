# from django.shortcuts import render
# from django.shortcuts import render,get_object_or_404,redirect
# from .models import Administration
# from django.views.generic import ListView,DeleteView
# from django.db.models import Q
# from django.views.generic.edit import CreateView,UpdateView,DeleteView
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
# from django.urls import reverse_lazy
# from django.contrib import messages
# from django.http import HttpResponse

# # Create your views here.
# def login(request):

#     return render(request,'registration/login.html')

from django.shortcuts import render
from .models import Administration
from django.urls import reverse_lazy
from django.contrib.auth.models import AnonymousUser
from django.views.decorators.cache import cache_control



# Create your views here.
# from django.shortcuts import render

# # Create your views here.
# def login(request):
#     return render(request,'registration/login.html')
from django.http import *
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

def login(request):
    print("===============")
   # username = password = ''
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        # projection = ['Administration.administration_administration.*']
        # sql = """SELECT * FROM administration_administration WHERE email="""+username
        # print(sql)
        for p in Administration.objects.raw('SELECT * FROM administration_administration'):
            if(p.email==username):
                if(p.password==password):
                    request.session['admin_id']=p.id
                    request.session['admin_name']=p.name
                    print(request.session.get('admin_name'))
                    return redirect('admin_home')

        # Administration.objects.filter(email=username, password=password).exists()
        # Administration.objects.filter(email=request.POST.get['username'], password=request.POST.get['password']).exists()
        #user = authenticate(username=username, password=password)
       # if user is not None:
            #if user.is_active:
                #login(request, user)
               # return HttpResponseRedirect('/')
    return render(request,'registration/login.html',{})

def admin_home(request):
    return render(request,'admin_home.html')

# @cache_control(no_cache=True, must_revalidate=True)
def logout(request):
    try:
        request.session.clear()
        request.user = AnonymousUser()
        return redirect('home')
        # # return HttpResponse(reverse('home'))
    except:
        return HttpResponse('error')