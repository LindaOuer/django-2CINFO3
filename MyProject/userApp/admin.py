from django.contrib import admin
from .models import Participant, Reservation

# Register your models here.

admin.site.register(Participant)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('conference', 'participant', 'confirmed',)
    actions = ['confirm_action',]
    def confirm_action(self, request, queryset):
        queryset.update(confirmed=True)
        self.message_user(request, "Selected reservations have been confirmed")
    confirm_action.short_description = "Confirm reservations"


admin.site.register(Reservation, ReservationAdmin)