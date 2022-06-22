from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('candidate', views.candidate, name='candidate'),
    path('create_portfolio', views.create_portfolio, name='create_portfolio'),
    path('<int:pk>', views.job_detail.as_view(), name='job_detail' ),
    path('<int:pk>/update', views.job_update.as_view(), name='job_update')
]
