from django.shortcuts import render
from apps.workshops.models import Workshop


def home(request):

    upcoming_workshops = Workshop.objects.filter(
        status="published"
    ).order_by("date")[:3]

    return render(
        request,
        "core/home.html",
        {
            "upcoming_workshops": upcoming_workshops
        }
    )
