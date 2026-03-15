from django.contrib import admin
from django.utils.html import format_html
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):

    list_display = (
        "image_preview",
        "title",
        "workshop",
        "featured",
        "created_at",
    )

    list_filter = (
        "featured",
        "workshop",
    )

    search_fields = (
        "title",
        "caption",
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px;border-radius:4px;" />',
                obj.image.url
            )
        return "-"
