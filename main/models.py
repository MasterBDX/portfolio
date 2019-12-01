from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	img = models.ImageField(upload_to='project_imgs')
	github = models.URLField(max_length=255,null=True,blank=True)
	live = models.URLField(max_length=255,null=True,blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now= True)
