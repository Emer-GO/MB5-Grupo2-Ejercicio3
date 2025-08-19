from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),       # 👈 index principal
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
path('register/', views.student_create, name='register'),


    path('listar/', views.student_list, name='student_list'),
    path('nuevo/', views.student_create, name='student_create'),
    path('editar/<int:pk>/', views.student_update, name='student_update'),
    path('eliminar/<int:pk>/', views.student_delete, name='student_delete'),
]
