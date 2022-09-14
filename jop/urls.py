from django.urls import path

from . import views

urlpatterns = [
    path('', views.job_list, name='index'),
    path('add_job',views.add_job , name='add_job'),
    path('<slug:slug>',views.job_detail , name='job_detail'),
    
]