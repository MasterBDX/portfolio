from django.db import models
from django_countries.fields import CountryField

from .utils import get_propic_name

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to=get_propic_name)
    github = models.URLField(max_length=255, null=True, blank=True)
    live = models.URLField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255,
                            blank=True,
                            null=True)
    # skill_color = models.CharField(max_length=255,default='')
    order = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    overview = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True, null=True)
    
    phone_number = models.CharField(max_length=255,
                            blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



class Location(models.Model):
    country = CountryField(default='LY')
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255,null=True,
                                            blank=True)
    province = models.CharField(max_length=255,null=True,
                                            blank=True)
    township = models.CharField(max_length=255,null=True,
                                            blank=True)

    def __str__(self):
        return self.country.name