from django.contrib import admin
from apps.reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "workshop",
        "rating",
        "is_featured"
    )

    list_filter = ("rating", "is_featured")