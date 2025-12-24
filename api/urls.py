from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.studentsView, name='studentview'),
    path('student/<int:pk>/', views.studentDetailView, name='studentDetailView'),
    
    path('employees/', views.Employees.as_view() , name='Employees'),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view() , name='EmployeeDetail'),
]
