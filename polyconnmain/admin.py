from django.contrib import admin
from .models import District, User, Cafe, Reservation, Event

# Register your models here.
admin.site.register(District)
admin.site.register(User)
admin.site.register(Cafe)
admin.site.register(Reservation)
admin.site.register(Event)