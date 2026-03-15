from django.db import models


class SiteSettings(models.Model):

    about_text = models.TextField()

    about_image = models.ImageField(
        upload_to="site/",
        blank=True,
        null=True
    )

    hero_image = models.ImageField(
        upload_to="site/",
        blank=True,
        null=True
    )

    contact_email = models.EmailField()

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    instagram = models.URLField(blank=True)

    linktree = models.URLField(blank=True)

    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name_plural = "Site Settings"