import os
from django.http import HttpResponse
from django.shortcuts import render
from .version import get_application_version_hash


def base(request):
    return render(request, 'base.html')


def version(request):
    return HttpResponse(get_application_version_hash(), content_type='text/plain')
