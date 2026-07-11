from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication
from .forms import JobForm

# READ
def job_list(request):
    jobs = JobApplication.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

# CREATE
def add_job(request):
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('job_list')
    return render(request, 'job_form.html', {'form': form})

# UPDATE
def update_job(request, id):
    job = get_object_or_404(JobApplication, id=id)
    form = JobForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        return redirect('job_list')
    return render(request, 'job_form.html', {'form': form})

# DELETE
def delete_job(request, id):
    job = get_object_or_404(JobApplication, id=id)
    job.delete()
    return redirect('job_list')