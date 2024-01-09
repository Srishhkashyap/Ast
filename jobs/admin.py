from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    search_fields = ['title', 'location']
    list_display = ['title', 'location', 'salary']
    list_filter = ['location']

admin.site.register(Job, JobAdmin)
