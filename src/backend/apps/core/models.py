from django.db import models

class Persona(models.Model):
    rut = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Proyecto(models.Model):
    id_proyecto = models.CharField(max_length=12)
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    
class ClientProject(models.Model):
    client = models.ForeignKey(Persona, on_delete=models.CASCADE)
    project = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    notes = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.client.name} - {self.project.name}"