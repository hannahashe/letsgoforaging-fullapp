from django.db import models
from apps.workshops.models import Workshop


# Create your models here.


class GalleryImage(models.Model):

    title = models.CharField(max_length=255, blank=True)

    image = models.ImageField(upload_to="gallery/")

    caption = models.TextField(blank=True)

    workshop = models.ForeignKey(
        Workshop,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="gallery_images"
    )

    featured = models.BooleanField(
        default=False,
        help_text="Show on homepage or promotional sections"
    )

    order = models.PositiveIntegerField(
        default=0,
        help_text="Lower numbers appear first"
    )

    is_public = models.BooleanField(
        default=True,
        help_text="Visible to all users if True, otherwise only staff can see"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        if self.title:
            return self.title
        return f"Image {self.id}"
