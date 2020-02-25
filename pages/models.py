from django.db import models

# Create your models here.
class About(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Work(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True) #TinyMCE

    def __str__(self):
        return self.title

class Expert(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True) #TinyMCE

    def __str__(self):
        return self.name