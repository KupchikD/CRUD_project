from django.shortcuts import render, get_object_or_404
from .models import Jobs



# Create your views here.
def home(request):
    jobs = Jobs.objects.all()
    return render(request, 'jobs/home.html', {'jobs':jobs})

def detail(request, job_id):
    job = get_object_or_404(Jobs, pk = job_id)
    return render(request, 'jobs/detail.html', {'job':job})