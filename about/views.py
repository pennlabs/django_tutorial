from django.shortcuts import render
from about.models import Project

def splash(request):
    projects = Project.objects.all()
    return render(request, "splash.html", {"projects": projects})