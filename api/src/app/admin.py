from django.contrib import admin
from .models import Task, Work

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'completion', 'time_expected', 'id_parent', 'log_create', 'log_modify')
    list_filter = ('completion', 'id_parent')
    search_fields = ('name', 'description')
    ordering = ('-log_create',)

class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_started', 'time_worked', 'id_task', 'log_create', 'log_modify')
    list_filter = ('id_task',)
    search_fields = ('name', 'description')
    ordering = ('-log_create',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Work, WorkAdmin)
