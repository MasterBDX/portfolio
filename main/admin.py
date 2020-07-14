from django.contrib import admin

from .models import Project, Skill,Location,Info

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Location)
admin.site.register(Info)