
from django.contrib import admin

from .models import WasteContainer, Waste, Comment, Profile


class WasteContainerAdmin(admin.ModelAdmin):
    list_display = ('cont_type',)


class WasteAdmin(admin.ModelAdmin):
    list_display = ('waste_name',)


admin.site.register(WasteContainer, WasteContainerAdmin)
admin.site.register(Waste, WasteAdmin)
admin.site.register(Comment)
admin.site.register(Profile)

# Register your models here.
