from django.db import models
from django.utils.text import slugify
from apps.workshops.models import Workshop
from apps.core.models import Tag


class BlogPost(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=255)

    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True
    )

    content = models.TextField()

    excerpt = models.TextField(
        blank=True,
        help_text="Short summary used on blog listings"
    )

    featured_image = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True
    )

    workshop = models.ForeignKey(
        Workshop,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blog_posts",
        help_text="Optional workshop related to this post"
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft"
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="blog_posts"
        )

    published_date = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_date"]

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
