from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Results
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from django.contrib import messages


# Create your views here.

def results(request):
    rolno=request.session.get('roolno_')
    for p in Results.objects.raw('SELECT * FROM results_results'):
        if(p.roolno==rolno):
            context={
                'result_marks':p
            }
            print(p.marks)
            return render(request,'view_result.html',context)
    return render(request,'student_home.html')

    


class add_marks(CreateView):
    model=Results
    print('------hh----')
    template_name='add_marks.html'
    fields=['name','roolno','department','semister','subjects','marks','pass_fail']
    def form_valid(self,form):
        instance=form.save(commit=False)
        print('cominge----------')
        instance.save()
        messages.success(self.request,'your contact added sucessfully')
        return redirect('lecturer_home')

