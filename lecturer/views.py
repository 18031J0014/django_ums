from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Lecturer 
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse_lazy

# Create your views here.

def lecturer_home(request):
    return render(request,'lecturer_home.html',{})

def view_lecturer_profile(request):
    id=request.session.get('id_')
    stud=Lecturer.objects.get(pk=id)
    context={
        'stu':stud
    }
    return render(request,'view_lecturer_profile.html',context)
class add_lecturer(CreateView):
    model=Lecturer
    template_name='add_lecturer.html'
    fields=['name','email','phone','info','gender','department','address','password','image']
    def form_valid(self, form):
        self.object = form.save(commit = False)
        form.save()
        return redirect('admin_home')
    # def form_valid(self,form):
    #     instance=form.save(commit=False)
    #     print("******************************************************************************8")
    #     instance.save()
    #     messages.success(self.request,'your contact added sucessfully')
    #     return super(add_lecturer, self).form_valid(form)

# def view_lecturer(request):
#     context = {
#         'lecturers':Lecturer.objects.all()
#     }
#     print('coming')
#     return render(request,'view_lecturer.html',context)

class view_lecturer(ListView):
    template_name='view_lecturer.html'
    model=Lecturer
    context_object_name='lecturers'

    def get_queryset(self):
        lecturers=super().get_queryset()
        return lecturers

class view_lecturer_detail(DetailView):
    template_name='view_lecturer_detail.html'
    model=Lecturer
    context_object_name='lecturer'

class delete_lecturer(DeleteView):
    model=Lecturer
    template_name='delete_lecturer.html'
    success_url='/'

    def delete(self,request,*args,**kwargs):
        messages.success(self.request,'Your Lecturer has been saved succesfully deleted!')
        return super().delete(self,request,*args,**kwargs)


def lecturer_login(request):
    
   # username = password = ''
    if request.method=="POST":
        print()
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        # projection = ['Administration.administration_administration.*']
        # sql = """SELECT * FROM administration_administration WHERE email="""+username
        # print(sql)
        for p in Lecturer.objects.raw('SELECT * FROM lecturer_lecturer'):
            if(p.email==username):
                if(p.password==password):
                    request.session['id_']=p.id
                    request.session['dept_']=p.department
                    request.session['name_']=p.name
                    print(request.session.get('dept_'))
                    return redirect('lecturer_home')

        # Administration.objects.filter(email=username, password=password).exists()
        # Administration.objects.filter(email=request.POST.get['username'], password=request.POST.get['password']).exists()
        #user = authenticate(username=username, password=password)
       # if user is not None:
            #if user.is_active:
                #login(request, user)
               # return HttpResponseRedirect('/')
    return render(request,'registration/lecturer_login.html',{})
    
class update_lecturer(UpdateView):
    model = Lecturer
    template_name = 'update_lecturer.html'
    fields = ['name','email','phone','info','gender','image','password','address']
    success_url = '/'

    def form_valid(self,form):
        instance = form.save()
        messages.success(self.request,'Your Contact has been saved succesfully updated!')
        return redirect('lecturer_home')

def update(request):
    lid=request.session.get('id_')
    dept=request.session.get('dept_')

    context={
        'l_id':lid,
        'l_dept':dept
    }
    return render(request,'empty.html',context)