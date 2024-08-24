from django.db import models

class Work(models.Model):
    task = models.ForeignKey(Task, related_name='works', on_delete=models.CASCADE)
    description = models.TextField()
    time_worked = models.IntegerField(default=0)  # Tempo trabalhado em minutos
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.time_worked} minutos - {self.description}"
