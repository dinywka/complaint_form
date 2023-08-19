from django.contrib import admin
from django.urls import path
from complaint_form import views

urlpatterns = [
    path('', views.home),
    path('complaint/', views.complaint),
    path('list/', views.list)

]