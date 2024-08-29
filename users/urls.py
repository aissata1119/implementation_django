
from django.urls import path
from .views import index, add_user, update_user  


app_name="users"
urlpatterns = [
    path('', index, name='index'),
    path('add/', add_user, name='add_user'),
    path('update/<int:user_id>/', update_user, name='update_user'),
]
