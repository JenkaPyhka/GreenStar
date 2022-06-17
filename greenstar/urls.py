from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('candidate', views.candidate, name='candidate'),
    # path('job', views.job_details, name='job'),
    path('create_portfolio', views.create_portfolio, name='create_portfolio'),
    path('<int:pk>', views.job_detail.as_view(), name='job_detail' )
]
