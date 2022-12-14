from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .form import ApplyForm , JobForm
from .models import Job
from django.contrib.auth.decorators import login_required

def job_list(request):
    job_list = Job.objects.all()
    context = {'jobs' :job_list , }
    return render(request,'job/job_list.html',context)


def job_detail(request , slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            print('DOne')

    else:
        form = ApplyForm()


    context = {'job' : job_detail , 'form1':form}
    return render(request,'job/job_detail.html',context)

def add_job(request): 

    context = {'jobs' :add_job , } # template name
    return render(request,'job/add_job.html',context)

@login_required
def add_job(request):
    if request.method=='POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = JobForm()

    return render(request,'job/add_job.html',{'form':form})