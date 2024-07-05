from django.urls import path, include
from apps.core import views
from apps.core.views import (
    Persona_list, Persona_create, Persona_delete, Persona_update,
    project_list, project_create, project_delete, project_update,
    Clientproject_list, Clientproject_create, Clientproject_delete, Clientproject_update    
)

urlpatterns = [
    path('', views.index, name='index'),

    path('clientes/', views.clientes, name='clientes'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('cliente-proyecto/', views.cliente_proyecto, name='cliente-proyecto'),
    path('crud-cliente/', views.crud_cliente, name='crud_cliente'),
    path('crud-proyecto/', views.crud_proyecto, name='crud-proyecto'),
    path('crud-cliente-proyecto/', views.crud_cliente_proyecto, name='crud-cliente-proyecto'),

    path('clients/', Persona_list, name='client_list'),
    path('clients/create/', Persona_create, name='client_create'),
    path('clients/<int:pk>/edit/', Persona_update, name='client_update'),
    path('clients/<int:pk>/delete/', Persona_delete, name='client_delete'),

    path('projects/', project_list, name='project_list'),
    path('projects/create/', project_create, name='project_create'),
    path('projects/<int:pk>/edit/', project_update, name='project_update'),
    path('projects/<int:pk>/delete/', project_delete, name='project_delete'),

    path('clientprojects/', Clientproject_list, name='clientproject_list'),
    path('clientprojects/create/', Clientproject_create, name='clientproject_create'),
    path('clientprojects/<int:pk>/edit/', Clientproject_update, name='clientproject_update'),
    path('clientprojects/<int:pk>/delete/', Clientproject_delete, name='clientproject_delete'),
]