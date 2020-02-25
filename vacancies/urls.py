from django.urls import path
from . import views

urlpatterns = [

    path('vacancies', views.vacancies, name='vacancies'),
    path('vacancy/<str:pk>/', views.vacancy, name='vacancy'),
    
]
