from django.contrib import admin
from scraper.models import Algorithm

@admin.register(Algorithm)
class AlgorithmAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'description')

# admin.site.register(Algorithm,AlgorithmAdmin)

# Register your models here.
