from django.contrib import admin

from .models import Listing, Dutie, Academic, Skill, Benefit

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'vacancy_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('title',)
    search_fields = ('title', 'country', 'city', 'looking_for')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)

class DutieAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'position')
    list_display_links = ('id', 'role')
    list_filter = ('role', 'position')
    list_per_page = 25

admin.site.register(Dutie, DutieAdmin)

class AcademicAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'position')
    list_display_links = ('id', 'role')
    list_filter = ('role', 'position')
    list_per_page = 25

admin.site.register(Academic, AcademicAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'position')
    list_display_links = ('id', 'role')
    list_filter = ('role', 'position')
    list_per_page = 25

admin.site.register(Skill, SkillAdmin)

class BenefitAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'position')
    list_display_links = ('id', 'role')
    list_filter = ('role', 'position')
    list_per_page = 25

admin.site.register(Benefit, BenefitAdmin)
