from django.db import models

class Task(models.Model):
    id_parent = models.ForeignKey('self', null=True, blank=True, related_name='subtasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField(default=0)  # Percentual de conclusão (0-100)
    time_expected = models.IntegerField(default=0)  # Tempo esperado para conclusão em minutos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Work(models.Model):
    task = models.ForeignKey(Task, related_name='works', on_delete=models.CASCADE)
    description = models.TextField()
    time_worked = models.IntegerField(default=0)  # Tempo trabalhado em minutos
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.time_worked} minutos - {self.description}"
