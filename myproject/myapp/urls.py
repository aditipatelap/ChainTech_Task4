from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.home, name='submit_form'),  # URL for form submission
]
