from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(default=0)
    director = models.ForeignKey('Director', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(null=True, blank=0)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text
