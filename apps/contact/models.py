from django.db import models

# Create your models here.


class ContactMessage(models.Model):

    name = models.CharField(max_length=255)

    email = models.EmailField()

    message = models.TextField()

    seen = models.BooleanField(default=False)

    replied = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"