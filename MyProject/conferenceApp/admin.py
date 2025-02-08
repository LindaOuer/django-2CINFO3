from django.contrib import admin
from .models import Conference, Category

# Register your models here.
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location', 'price')

admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Category)

