from django.contrib import admin

from .models import VideoGear 


class  VideoGearAdmin(admin.ModelAdmin):
    list_display = ('rental_tag', 'gear_type', 'fosdem_tag', 'state', 'notes')
    list_filter = ['state', 'gear_type']
    search_fields = ['rental_tag', 'fosdem_tag']

admin.site.register(VideoGear, VideoGearAdmin)

