from django.contrib import admin
from django.urls import path

from . import views

app_name = 'auth'

urlpatterns = [
    path('', views.taskList, name='taskList'),
    path('auth/registro', views.registro, name='registro'),
    path('auth/login', views.user_login, name='login'),
    path('auth/logout', views.user_logout),
    path('adicionarTarefa/', views.addTask),
    path('tarefa/<int:id_tarefa>', views.taskInfo),
    path('editarTarefa/<str:id_tarefa>', views.editTask),
    path('deletarTarefa/<int:id_tarefa>', views.deleteTask),
    path('about/', views.about)
]