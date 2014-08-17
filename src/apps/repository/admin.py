from django.contrib import admin
from apps.lib.admin import model_admin
from .models import Item, ItemGroup, ItemGroupEntry, ItemTag, ItemType


@model_admin(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = 'id', 'path', 'created_at'


@model_admin(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = 'id', 'mime_type', 'extension'


@model_admin(ItemGroup)
class ItemGroup(admin.ModelAdmin):
    list_display = 'id', 'description', 'created_at'


@model_admin(ItemGroupEntry)
class ItemGroupEntry(admin.ModelAdmin):
    list_display = 'id', 'item_group', 'item', 'position', 'created_at'


@model_admin(ItemTag)
class ItemTag(admin.ModelAdmin):
    list_display = 'id', 'label', 'created_at'
