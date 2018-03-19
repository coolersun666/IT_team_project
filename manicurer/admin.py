from django.contrib import admin

# Register your models here.
from manicurer.models import Picture, UserProfile

class PictureAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'NumberOfRates','avgrate')



admin.site.register(Picture,PictureAdmin)
admin.site.register(UserProfile)
