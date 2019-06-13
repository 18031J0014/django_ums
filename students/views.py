from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Student
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from django.contrib import messages
from urllib import request


# Create your views here.


def student_home(request):
    return render(request,'student_home.html')

class add_student(CreateView):
    model=Student
    template_name='add_student.html'
    fields=['name','email','phone','rollno','gender','department','address','password','image']
    def form_valid(self,form):
        instance=form.save(commit=False)
        #print("svrjfjabybfs")
        instance.save()
        messages.success(self.request,'your contact added sucessfully')
        return redirect('lecturer_home')


class view_student(ListView):
    template_name='view_lecturer_students.html'
    model=Student
    context_object_name='students'

    def get_queryset(self):
        # lid=self.request.session.get('id_')
        # print(lid)
        students=super().get_queryset()
        return students

# def view_student(request,id):
#     context = {
#         model:Student
#         context_object_name:'students'
#         'contact':get_object_or_404(Contact,pk=id)
#     }
#     return render(request,'view_student.html',context)


def view(request):
    lid=request.session.get('id_')
    dept=request.session.get('dept_')
    print(lid)
    print(dept)
    context={
        'l_id':lid,
        'l_dept':dept
    }
    return render(request,'empty.html',context)


class view_student_detail(DetailView):
    template_name='view_student_detail.html'
    model=Student
    context_object_name='student'
    print('details ')


def view_student_profile(request):
    id=request.session.get('id_')
    stud=Student.objects.get(pk=id)
    context={
        'stu':stud
    }
    return render(request,'view_student_profile.html',context)



# class view_student_profile(DetailView):
#     template_name='view_student_profile.html'
#     model=Student
#     context_object_name='student'
#     print('details ')

# class delete_student(DeleteView):
#     model=Student
#     template_name='delete_student.html'
#     success_url='/'

#     def delete(self,request,*args,**kwargs):
#         print('delete')
#         messages.success(self.request,'Your Lecturer has been saved succesfully deleted!')
#         return super().delete(self,request,*args,**kwargs)

def delete_student(request,pk=None):
    if pk:
        one_task = Student.objects.get(id = pk)
        one_task.delete()
        return render(request,'lecturer_home.html')



def student_login(request):
    
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
        for p in Student.objects.raw('SELECT * FROM students_student'):
            if(p.email==username):
                if(p.password==password):
                    request.session['roolno_']=p.rollno
                    request.session['name_']=p.name
                    request.session['id_']=p.id
                    request.session['dept_']=p.department
                    print(request.session.get('dept_'))
                    return redirect('student_home')
    return render(request,'registration/student_login.html',{})

class update_student(UpdateView):
    model = Student
    template_name = 'update_student.html'
    fields = ['name','email','phone','info','gender','image','password','address']
    success_url = '/'

    def form_valid(self,form):
        instance = form.save()
        messages.success(self.request,'Your Contact has been saved succesfully updated!')
        return redirect('student_home')

def update(request):
    lid=request.session.get('id_')
    dept=request.session.get('dept_')

    context={
        'l_id':lid,
        'l_dept':dept
    }
    return render(request,'empty.html',context)

def feepayment(request):
    return render(request,'feepayment.html',{})

def view_department_students(request,pk=None):
    if pk==1:
        dept = 'IT'
        for p in Student.objects.raw('SELECT * FROM students_student'):
            if(p.department==dept):
                context={
                    'student':p
                }
        return render(request,'view_department_students.html',context)
    if pk==2:
        dept = 'CSE'
        for p1 in Student.objects.raw('SELECT * FROM students_student'):
            if(p1.department==dept):
                context={
                    'student':p1
                }
        return render(request,'view_department_students.html',context)
    if pk==3:
        dept = 'ECE'
        for p2 in Student.objects.raw('SELECT * FROM students_student'):
            if(p2.department==dept):
                context={
                    'student':p2
                }
        return render(request,'view_department_students.html',context)
    if pk==4:
        dept = 'EEE'
        for p3 in Student.objects.raw('SELECT * FROM students_student'):
            if(p3.department==dept):
                context={
                    'student':p3
                }
        return render(request,'view_department_students.html',context)

