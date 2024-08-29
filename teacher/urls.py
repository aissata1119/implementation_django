from turtle import update
from django.urls import path
from .views import index
from .views import add_teacher
from .views import update
from.views import delete

app_name = 'teacher'
urlpatterns = [
    
    path('', index, name='index'),
    path('add', add_teacher, name='add'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>',delete,name ='delete')
    
]
