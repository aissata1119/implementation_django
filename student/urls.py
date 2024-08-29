from django.urls import path
from .views import index
from .views import add_student
from .views import update,delete

app_name = 'student'
urlpatterns = [
    
    path('', index, name='index'),
    path('add', add_student, name='add'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),

    
]
