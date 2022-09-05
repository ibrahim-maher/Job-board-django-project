from django.http import HttpResponse

def job_list(request):
    job_list = Job.objects.all()

    context = {'jobs' :job_list , } # template name
    return render(request,'job/job_list.html',context)
