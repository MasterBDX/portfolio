from django.shortcuts import render
from django.views.generic import ListView

from .forms import Contact
from .models import Project


def home_view(request):
	projects = Project.objects.all()
	form = Contact()
	
	context = {'projects':projects,'form':form}
	return render(request,'main/home.html',context)
