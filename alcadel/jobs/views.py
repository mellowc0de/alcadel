from django.shortcuts import render

from .models import Job, MainSlider

def home(request):
    jobs = Job.objects
    sliders = MainSlider.objects
    return render(request, 'jobs/home.html', {'jobs':jobs, 'sliders':sliders})
