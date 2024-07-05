from django import forms
from apps.core.models import Persona, Proyecto, ClientProject

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['rut','name', 'email', 'number']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['id_proyecto', 'name', 'start_date', 'end_date']

class ClientProjectForm(forms.ModelForm):
    class Meta:
        model = ClientProject
        fields = ['client', 'project', 'notes', 'link']
