from django.db import models
from apps.workshops.models import Workshop


class Review(models.Model):

    workshop = models.ForeignKey(
        Workshop,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviews"
    )

    name = models.CharField(max_length=255)

    content = models.TextField()

    rating = models.IntegerField()

    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.rating}"