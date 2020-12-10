from django.db import models
from django_countries.fields import CountryField
from django_resized import ResizedImageField

from .utils import get_propic_name

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = ResizedImageField(size=[696, 500], upload_to=get_propic_name)
    # img = models.ImageField(upload_to=get_propic_name)
    github = models.URLField(max_length=255, null=True, blank=True)
    live = models.URLField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['-order']

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


class Info(models.Model):
    facebook = models.URLField(max_length=255, null=True, blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)
    linkedin = models.URLField(max_length=255, null=True, blank=True)
    github = models.URLField(max_length=255, null=True, blank=True)
    
    phone_number = models.CharField(max_length=255,
                            blank=True,null=True)
    
    overview = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Location(models.Model):
    country = CountryField(default='LY')
    city = models.CharField(max_length=255)
    province = models.CharField(
                                max_length=255,
                                null=True,
                                blank=True
                                )
    township = models.CharField(max_length=255,null=True,
                                            blank=True)

    street = models.CharField(max_length=255,null=True,
                                            blank=True)

    house_num = models.CharField(max_length=255,null=True,
                                            blank=True)
                                            
    zip_code = models.CharField(max_length=255,null=True,
                                            blank=True)

    def __str__(self):
        return self.country.name