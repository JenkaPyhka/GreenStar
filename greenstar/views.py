from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import portfolio
from django.views.generic import DetailView, UpdateView
from .forms import portfolioFrom


class job_detail(DetailView):
    model = portfolio
    template_name = 'greenstar/job_details.html'
    context_object_name = 'portfolio'

class job_update(UpdateView):
    model = portfolio
    template_name = 'greenstar/update.html'
    form_class = portfolioFrom

def index(request):
    portfolios = portfolio.objects.order_by('-date')[:4]
    return render(request, 'greenstar/index.html', {'portfolios': portfolios})

def candidate(request):
    portfolios = portfolio.objects.order_by('-date')
    return render(request, 'greenstar/candidate.html', {'portfolios': portfolios})

def create_portfolio(request):
    error = ''
    if request.method == "POST":
        form = portfolioFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма заполнена не верно"
    form = portfolioFrom()
    data = { 
        'form': form,
        'error': error
    }
    return render(request, 'greenstar/create.html', data)