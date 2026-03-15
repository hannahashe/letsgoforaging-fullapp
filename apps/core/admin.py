from django.contrib import admin
from .models import SiteSettings
from apps.contact.models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "seen",
        "replied",
        "created_at"
    )

    list_filter = ("seen", "replied")

    search_fields = ("name", "email")


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    fieldsets = (

        ("About", {
            "fields": (
                "about_text",
                "about_image",
            )
        }),

        ("Homepage", {
            "fields": (
                "hero_image",
            )
        }),

        ("Contact", {
            "fields": (
                "contact_email",
                "contact_phone",
            )
        }),

        ("Social", {
            "fields": (
                "instagram",
                "linktree",
            )
        }),

    )
