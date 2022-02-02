from django.contrib import admin

from apps.cast.models import Location, Character, House

admin.site.register(Location)
admin.site.register(House)
admin.site.register(Character)