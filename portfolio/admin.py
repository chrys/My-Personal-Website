from django.contrib import admin
from .models import MyProject

@admin.register(MyProject)
class MyProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'github_repository', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
