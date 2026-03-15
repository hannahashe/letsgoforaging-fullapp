from django.shortcuts import render, get_object_or_404
from apps.workshops.models import Workshop
from taggit.models import Tag
from apps.workshops.models import Workshop
from apps.blog.models import BlogPost


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


def tag_page(request, slug):

    tag = get_object_or_404(Tag, slug=slug)

    workshops = Workshop.objects.filter(tags__slug=slug)
    posts = BlogPost.objects.filter(tags__slug=slug)

    return render(
        request,
        "core/tag_page.html",
        {
            "tag": tag,
            "workshops": workshops,
            "posts": posts
        }
    )