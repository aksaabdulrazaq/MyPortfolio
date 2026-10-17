from django.shortcuts import render

from bio.models import Bio
from education.models import Degree
from experience.models import Project
from skills.models import Skill


def home(request):
    context = {
        "bios": Bio.objects.all(),
        "degrees": Degree.objects.all(),
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
    }
    return render(request, "index.html", context)
