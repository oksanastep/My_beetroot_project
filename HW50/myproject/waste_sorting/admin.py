
from django.contrib import admin

from .models import Container, Waste, Comment, Profile


class WasteContainerAdmin(admin.ModelAdmin):
    list_display = ('type',)


class WasteAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Container, WasteContainerAdmin)
admin.site.register(Waste, WasteAdmin)
admin.site.register(Comment)
admin.site.register(Profile)

# Register your models here.
