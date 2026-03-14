from django.db import models


class SiteSettings(models.Model):

    site_name = models.CharField(max_length=200)

    hero_title = models.CharField(max_length=200)

    hero_subtitle = models.TextField()

    about_text = models.TextField()

    contact_email = models.EmailField()

    instagram_url = models.URLField(blank=True)

    def __str__(self):
        return self.site_name
