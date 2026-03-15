from django.contrib import admin
from .models import Workshop
from django.utils.html import format_html
from apps.gallery.models import GalleryImage


class GalleryImageInline(admin.TabularInline):

    model = GalleryImage
    extra = 1

    readonly_fields = ("image_preview",)

    fields = (
        "image",
        "image_preview",
        "caption",
        "order",
        "featured",
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px;border-radius:4px;" />',
                obj.image.url
            )
        return "-"


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):

    inlines = [GalleryImageInline]

    list_display = (
        "image_preview",
        "title",
        "date",
        "start_time",
        "location_name",
        "price",
        "spaces_available",
        "status",
    )

    list_filter = (
        "status",
        "season",
        "date",
    )

    search_fields = (
        "title",
        "location_name",
    )

    prepopulated_fields = {"slug": ("title",)}

    ordering = ("date",)

    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Workshop Info", {
            "fields": (
                "title",
                "slug",
                "description",
                "season",
                "tags",
                "status",
            )
        }),

        ("Schedule", {
            "fields": (
                "date",
                "start_time",
            )
        }),

        ("Location", {
            "fields": (
                "location_name",
                "location_description",
                "location_address",
            )
        }),

        ("Booking", {
            "fields": (
                "price",
                "max_participants",
                "spaces_available",
                "ticket_url",
            )
        }),

        ("Media", {
            "fields": (
                "image",
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
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px;border-radius:4px;" />',
                obj.image.url
                )
            return "-"
