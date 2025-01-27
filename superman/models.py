from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)  # Name field (required)
    email = models.EmailField()  # Email field (required)
    phone = models.CharField(max_length=15, blank=True, null=True)  # Phone field (optional)
    discribe = models.TextField()  # Description field (required)
    date = models.DateTimeField()  # Date field (required)

    def __str__(self):
        return self.name  # Human-readable name for the object
