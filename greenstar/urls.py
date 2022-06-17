from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('candidate', views.candidate, name='candidate'),
    path('job', views.job_details, name='job')
]
