from django.shortcuts import render, get_object_or_404, redirect
from apps.core.models import Persona, Proyecto, ClientProject
from apps.core.forms import PersonaForm, ProjectForm, ClientProjectForm

def index(request):
    template_name = "index.html"
    context = {} 
    return render(request, template_name, context)

def clientes(request):
    template_name = "clientes.html"
    context = {}
    return render (request, template_name,  context)

def proyectos(request):
    template_name = "proyectos.html"
    context = {}
    return render (request, template_name,  context)

def cliente_proyecto(request):
    template_name = "cliente-proyecto.html"
    context = {}
    return render (request, template_name,  context)

def crud_cliente(request):
    template_name = "crud-clientes.html"
    context = {}
    return render (request, template_name,  context)

def crud_proyecto(request):
    template_name = "crud-proyecto.html"
    context = {}
    return render (request, template_name,  context)

def crud_cliente_proyecto(request):
    template_name = "crud-cliente-proyecto.html"
    context = {}
    return render (request, template_name,  context)

# Persona Views
def Persona_list(request):
    Personas = Persona.objects.all()
    return render(request, 'Persona_list.html', {'Personas': Personas})

def Persona_create(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Persona_list')
    else:
        form = PersonaForm()
    return render(request, 'Persona_form.html', {'form': form})

def Persona_update(request, pk):
    Persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=Persona)
        if form.is_valid():
            form.save()
            return redirect('Persona_list')
    else:
        form = PersonaForm(instance=Persona)
    return render(request, 'Persona_form.html', {'form': form})

def Persona_delete(request, pk):
    Persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        Persona.delete()
        return redirect('Persona_list')
    return render(request, 'Persona_confirm_delete.html', {'object': Persona})


# Project Views
def project_list(request):
    projects = Proyecto.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

def project_update(request, pk):
    project = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_form.html', {'form': form})

def project_delete(request, pk):
    project = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'project_confirm_delete.html', {'object': project})


# ClientProject Views
def Clientproject_list(request):
    Clientprojects = ClientProject.objects.all()
    return render(request, 'Clientproject_list.html', {'Clientprojects': Clientprojects})

def Clientproject_create(request):
    if request.method == 'POST':
        form = ClientProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clientproject_list')
    else:
        form = ClientProjectForm()
    return render(request, 'Clientproject_form.html', {'form': form})

def Clientproject_update(request, pk):
    Clientproject = get_object_or_404(ClientProject, pk=pk)
    if request.method == 'POST':
        form = ClientProjectForm(request.POST, instance=Clientproject)
        if form.is_valid():
            form.save()
            return redirect('Clientproject_list')
    else:
        form = ClientProjectForm(instance=Clientproject)
    return render(request, 'Clientproject_form.html', {'form': form})

def Clientproject_delete(request, pk):
    Clientproject = get_object_or_404(ClientProject, pk=pk)
    if request.method == 'POST':
        Clientproject.delete()
        return redirect('Clientproject_list')
    return render(request, 'Clientproject_confirm_delete.html', {'object': ClientProject})