from django.db import models
from datetime import datetime
from .validators import validate_file_size

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
    doc_file = models.FileField(upload_to='documents/%Y/%m/%d/', validators=[validate_file_size], null=True)

    def __str__(self):
        return self.name