import os
import subprocess
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def base(request):
    return render(request, 'base.html')


def version(request):
    try:
        cmd = '/usr/bin/git', 'rev-parse', 'HEAD'
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()[0].strip()
        if (process.returncode != 0) or (not stdout.strip()) or stderr.strip():
            raise Exception

        version = stdout.strip()

    except:
        version = '(UNKNOWN)'

    return HttpResponse(version)
