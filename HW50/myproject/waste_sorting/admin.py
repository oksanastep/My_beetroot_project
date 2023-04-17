
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Container, Waste, Comment


class WasteContainerAdmin(admin.ModelAdmin):
    list_display = ('type',)


class WasteAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'date_created')


admin.site.register(Container, WasteContainerAdmin)
admin.site.register(Waste, WasteAdmin)
admin.site.register(Comment, CommentAdmin)




# Register your models here.
