from django.apps import AppConfig

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    verbose_name = "Task Management App"

    def ready(self):
        # Aqui você pode incluir qualquer código que precisa ser executado
        # quando o aplicativo for carregado, como sinais ou inicializadores.
        pass
