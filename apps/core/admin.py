from django.contrib import admin
from .models import SiteSettings


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