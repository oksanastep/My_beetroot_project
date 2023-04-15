
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Container, Waste


class WasteContainerAdmin(admin.ModelAdmin):
    list_display = ('type',)


class WasteAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Container, WasteContainerAdmin)
admin.site.register(Waste, WasteAdmin)




# Register your models here.
