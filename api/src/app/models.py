from django.db import models

class Task(models.Model):
    id_parent = models.IntegerField(default=0)
    
    completion = models.IntegerField(default=0)
    time_expected = models.IntegerField(default=0)
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')

    log_create = models.DateTimeField(auto_now_add=True)
    log_modify = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Work(models.Model):
    id_task = models.IntegerField(default=0)
    
    time_started = models.IntegerField(default=0)
    time_worked = models.IntegerField(default=0)
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')

    log_create = models.DateTimeField(auto_now_add=True)
    log_modify = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
