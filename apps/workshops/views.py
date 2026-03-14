from django.shortcuts import render, get_object_or_404
from .models import Workshop


def workshop_list(request):

    workshops = Workshop.objects.filter(
        status="published"
        ).order_by("date")

    return render(
        request,
        "workshops/workshop_list.html",
        {"workshops": workshops}
    )


def workshop_detail(request, slug):

    workshop = get_object_or_404(
        Workshop,
        slug=slug,
        status="published"
    )

    return render(
        request,
        "workshops/workshop_detail.html",
        {"workshop": workshop}
    )
