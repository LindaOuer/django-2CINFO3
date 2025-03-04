from django.urls import path
from .views import *

urlpatterns = [
    path('home/', index, name='app_index'),
    path('list/', listStudents, name='app_listStudents'),
    path('details/<int:id>', detailsStudent, name='app_detailStudent'),
]