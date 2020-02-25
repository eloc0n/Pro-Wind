from django.db import models
from datetime import datetime

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=120)
    looking_for = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    position = models.CharField(max_length=120, blank=True)
    vacancy_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Dutie(models.Model):
    role = models.ForeignKey(Listing, on_delete=models.CASCADE)
    position = models.CharField(max_length=120, blank=True)
    duties = models.TextField(blank=True)

    def __str__(self):
        return self.position

class Academic(models.Model):
    role = models.ForeignKey(Listing, on_delete=models.CASCADE)
    position = models.CharField(max_length=120, blank=True)
    academics = models.TextField(blank=True)

    def __str__(self):
        return self.position

class Skill(models.Model):
    role = models.ForeignKey(Listing, on_delete=models.CASCADE)
    position = models.CharField(max_length=120, blank=True)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.position

class Benefit(models.Model):
    role = models.ForeignKey(Listing, on_delete=models.CASCADE)
    position = models.CharField(max_length=120, blank=True)
    benefits = models.TextField(blank=True)

    def __str__(self):
        return self.position
