from http.client import HTTPResponse
from django.shortcuts import render
from .models import portfolio
from django.views.generic import DetailView

def index(request):
    portfolios = portfolio.objects.all()
    return render(request, 'greenstar/index.html', {'portfolios': portfolios})

def candidate(request):
    portfolios = portfolio.objects.all()
    return render(request, 'greenstar/candidate.html', {'portfolios': portfolios})

def job_details(request):
    portfolios = portfolio.objects.all()
    return render(request, 'greenstar/job_details.html', {'portfolios': portfolios})