from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.studentsView, name='studentview'),
    path('student/<int:pk>/', views.studentDetailView, name='studentDetailView'),
]
