from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Tag(models.Model):

    name = models.CharField(max_length=100)

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class TaggedItem(models.Model):

    tag = models.ForeignKey(
        "Tag",
        on_delete=models.CASCADE
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey(
        "content_type",
        "object_id"
    )

    def __str__(self):
        return f"{self.tag}"


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