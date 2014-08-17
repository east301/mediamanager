from django.db import models


class Item(models.Model):
    """Represents an item."""

    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=1024, unique=True)
    type = models.ForeignKey('ItemType', related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)


class ItemType(models.Model):
    """Represents a type of an item."""

    id = models.AutoField(primary_key=True)
    mime_type = models.CharField(max_length=128, unique=True)
    extension = models.CharField(max_length=128, unique=True)


class ItemGroup(models.Model):
    """Represents a group of items."""

    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1024, blank=True)
    items = models.ManyToManyField(Item, through='ItemGroupEntry', related_name='item_groups')
    created_at = models.DateTimeField(auto_now_add=True)


class ItemGroupEntry(models.Model):
    """Represents an entry of ItemGroup."""

    id = models.AutoField(primary_key=True)
    item_group = models.ForeignKey(ItemGroup, related_name='item_group_entries')
    item = models.ForeignKey(Item, related_name='item_group_entries')
    position = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = 'item_group', 'item'


class ItemTag(models.Model):
    """Represents a tag associated to items."""

    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=128, unique=True)
    items = models.ManyToManyField(Item, related_name='item_tags')
    created_at = models.DateTimeField(auto_now_add=True)
