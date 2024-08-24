from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import TaskViewSet, WorkViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'works', WorkViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
