from django.shortcuts import render
from apps.workshops.models import Workshop
from apps.blog.models import BlogPost
from apps.reviews.models import Review


def home(request):

    workshops = Workshop.objects.filter(
        status="published"
    ).order_by("date")[:3]

    posts = BlogPost.objects.filter(
        is_published=True
    )[:3]

    reviews = Review.objects.filter(
        is_featured=True
    )[:3]

    return render(
        request,
        "core/home.html",
        {
            "workshops": workshops,
            "posts": posts,
            "reviews": reviews
        }
    )
