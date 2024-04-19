from django.contrib import admin

from api.models import Palette

# Register your models here.
@admin.register(Palette)
class PaletteAdmin(admin.ModelAdmin):
    list_display = ['likes', 'color1', 'color2', 'color3', 'color4']