from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/')

    def __str__(self):
        return self.title
