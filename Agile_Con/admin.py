from django.contrib import admin

from .models import Presenter, Attendee, Presentation, CustomerOrder

class PresenterList(admin.ModelAdmin):
    list_display = ( 'presenter_id', 'name', 'user' )
    list_filter = ( 'presenter_id', 'name', 'user' )
    search_fields = ( 'presenter_id', 'name', 'user' )
    ordering = ['presenter_id']

class AttendeeList(admin.ModelAdmin):
    list_display = ( 'attendee_id', 'name', 'user' )
    list_filter = ( 'attendee_id', 'name', 'user' )
    search_fields = ( 'attendee_id', 'name', 'user' )
    ordering = ['attendee_id']

class PresentationList(admin.ModelAdmin):
    list_display = ( 'presenter_id', 'timeslot', 'cost' )
    list_filter = ( 'presenter_id', 'timeslot', 'cost' )
    search_fields = ( 'presenter_id', 'timeslot', 'cost' )
    ordering = ['presenter_id']

class CustomerOrderAdmin(admin.ModelAdmin):
    model = CustomerOrder


admin.site.register(CustomerOrder, CustomerOrderAdmin)
admin.site.register(Presenter)
admin.site.register(Attendee)
admin.site.register(Presentation)