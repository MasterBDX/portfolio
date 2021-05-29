from django.contrib import admin

from .models import Project, Skill,Location,Info

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['__str__','order']

admin.site.register(Project,ProjectAdmin)
admin.site.register(Skill)
admin.site.register(Location)
admin.site.register(Info)