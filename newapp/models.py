from django.db import models

# Create your models here.


class Review(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{self.name} — {self.rating}/5"