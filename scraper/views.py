from django.shortcuts import render
from django.http import HttpResponse
from scraper.models import Algorithm


def home(request):
    return HttpResponse("Welcome to the Mayo Clinic Algorithms!")

def algorithm_list(request):
    algorithms = Algorithm.objects.all()
    return render(request, 'scraper/algorithm_list.html', {'algorithms': algorithms})