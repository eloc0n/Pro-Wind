from django.urls import path

from . import views

urlpatterns = [
  path('contact/<str:pk>/', views.contact, name='contact')
]