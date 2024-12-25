from django.contrib import admin

# Register your models here.

from .models import Blog, Project, AboutMe

admin.site.register(Blog)
#admin.site.register(Service)
admin.site.register(AboutMe)
admin.site.register(Project)
