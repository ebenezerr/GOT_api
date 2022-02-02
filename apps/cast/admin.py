from django.contrib import admin

# Register your models here.
from apps.cast.models import Location, Character, House

admin.site.register(Location)
admin.site.register(House)
admin.site.register(Character)