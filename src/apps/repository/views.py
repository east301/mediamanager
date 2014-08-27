from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from apps.lib.template import render_to
from .item import generate_thumbnail_of_item
from .models import Item


@render_to('recent.html')
def recent(request):
    items = Item.objects.order_by('-created_at')[:30]
    return dict(items=items)


def thumbnail(request, id):
    item = get_object_or_404(Item, id=int(id))
    thumbnail = generate_thumbnail_of_item(item, 180, 160, 'png')
    return HttpResponse(thumbnail, content_type='image/png')
