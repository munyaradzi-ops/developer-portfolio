from django.shortcuts import render, redirect

from .models import ContactMessage
from core.models import Profile


def contact(request):

    profile = Profile.objects.first()

    if request.method == "POST":

        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        return redirect("contact")

    return render(
        request,
        "contact.html",
        {
            "profile": profile
        }
    )