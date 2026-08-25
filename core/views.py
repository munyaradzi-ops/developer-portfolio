from django.shortcuts import render
from .models import Profile, Skill
from projects.models import Project


def home(request):
    profile = Profile.objects.first()

    skills = Skill.objects.all()

    featured_projects = Project.objects.filter(
        featured=True
    ).order_by("-created_at")

    context = {
        "profile": profile,
        "skills": skills,
        "featured_projects": featured_projects,
    }

    return render(
        request,
        "home.html",
        context
    )


def about(request):
    profile = Profile.objects.first()

    context = {
        "profile": profile,
    }

    return render(
        request,
        "about.html",
        context
    )