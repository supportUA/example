from django.contrib import admin

from .models import *


class HeroAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'status')
    list_per_page = 15


admin.site.register(Hero, HeroAdmin)