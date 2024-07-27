from django.contrib import admin
from .models import Character, Bounty, Location, LogCharacter, Hunter, ClaimBounty
from django.utils.html import format_html


# Register your models here.
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('image_thumbnail', 'name', 'status', 'species', 'origin')
    ordering = ('status',)
    search_fields = ['name']
    list_filter = ('status', 'species',)

    readonly_fields = ('image_tag',)

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />', obj.image)
        return "-"

    image_thumbnail.short_description = 'Image'
admin.site.register(Character, CharacterAdmin)

class BountyAdmin(admin.ModelAdmin):
    list_display = ('character_id', 'search_status', 'amount', 'currency_type')
    ordering = ('search_status',)
    search_fields = ['character__name']
    list_filter = ('currency_type',)
admin.site.register(Bounty, BountyAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_location', 'dimension')
    ordering = ('name',)
    search_fields = ['name']
    list_filter = ('type_location',)
admin.site.register(Location, LocationAdmin)

class LogCharacterAdmin(admin.ModelAdmin):
    list_display = ('character_id', 'location_id', 'description', 'date_time')
    ordering = ('date_time',)
    search_fields = ['character__name', 'location__name']
    list_filter = ('date_time',)
admin.site.register(LogCharacter, LogCharacterAdmin)

class HunterAdmin(admin.ModelAdmin):
    list_display = ('image_thumbnail', 'name', 'nickname')
    ordering = ('name',)
    search_fields = ['name',]
    list_filter = ('name',)

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />', obj.image)
        return "-"

    image_thumbnail.short_description = 'Image'
admin.site.register(Hunter, HunterAdmin)

class ClaimBountyAdmin(admin.ModelAdmin):
    list_display = ('hunter_id', 'bounty_id', 'date_time', 'claimed')
    ordering = ('date_time',)
    search_fields = ['hunter_id', 'bounty_id']
    list_filter = ('date_time',)
admin.site.register(ClaimBounty, ClaimBountyAdmin)