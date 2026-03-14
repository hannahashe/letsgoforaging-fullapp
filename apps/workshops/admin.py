from django.contrib import admin
from .models import Workshop


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "date",
        "location_name",
        "price",
        "spaces_available",
        "status",
    )

    prepopulated_fields = {"slug": ("title",)}

    list_filter = ("status", "date")

    search_fields = ("title", "location_name")
