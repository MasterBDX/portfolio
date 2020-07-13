from django.contrib import admin

from .models import Project, Skill, AboutMe,Location

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(AboutMe)
admin.site.register(Location)