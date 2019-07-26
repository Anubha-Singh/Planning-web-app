
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='addTodo'),
    path('complete/<todo_id>', views.completeTodo, name='completeTodo'),
    path('deletecompleted', views.deletecompleted, name='deletecompleted'),
    path('deleteAll', views.deleteAll, name='deleteAll'),

]