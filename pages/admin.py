from django.contrib import admin
from .models import About, Work, Expert
# from tinymce.widgets import TinyMCE
# from django.db import models

# Register your models here.
# class WorkAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': TinyMCE()}
#     }

admin.site.register(Work)
admin.site.register(About)
admin.site.register(Expert)