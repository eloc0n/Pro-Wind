from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    vacancy = models.CharField(max_length=120)
    vacancy_id = models.IntegerField()
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    cover_letter = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name