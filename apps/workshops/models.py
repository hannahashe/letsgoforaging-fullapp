from django.db import models
from django.utils.text import slugify


class Workshop(models.Model):
    SEASON_CHOICES = [
        ("spring", "Spring"),
        ("summer", "Summer"),
        ("fall", "Fall"),
        ("winter", "Winter"),
    ] 

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
        ("cancelled", "Cancelled"),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    description = models.TextField()

    date = models.DateField()
    start_time = models.TimeField()
    season = models.IntegerField(choices=SEASON_CHOICES)

    location_name = models.CharField(max_length=255)
    location_description = models.TextField()
    location_address = models.CharField(max_length=300, blank=True)

    price = models.DecimalField(max_digits=6, decimal_places=2)

    max_participants = models.PositiveIntegerField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft"
    )

    spaces_available = models.PositiveIntegerField(blank=True, null=True)

    image = models.ImageField(upload_to="workshops/", blank=True, null=True)

    ticket_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date"]

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        if self.spaces_available is None:
            self.spaces_available = self.max_participants

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.date}"
