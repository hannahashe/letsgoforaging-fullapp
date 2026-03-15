from django.contrib import admin
from django.utils.html import format_html
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    list_display = (
        "image_preview",
        "title",
        "status",
        "published_date",
    )

    list_filter = ("status",)

    search_fields = ("title", "content")

    prepopulated_fields = {"slug": ("title",)}

    readonly_fields = ("created_at", "updated_at")

    fieldsets = (

        ("Post", {
            "fields": (
                "title",
                "slug",
                "excerpt",
                "content",
                "tags",
            )
        }),

        ("Media", {
            "fields": (
                "featured_image",
            )
        }),

        ("Related Workshop", {
            "fields": (
                "workshop",
            )
        }),

        ("Publishing", {
            "fields": (
                "status",
                "published_date",
            )
        }),

        ("System", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),

    )

    def image_preview(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" style="height:60px;border-radius:4px;" />',
                obj.featured_image.url
            )
        return "-"
