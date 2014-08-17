import subprocess
from django.conf import settings


def get_application_version_hash():
    """
    Gets version hash from VCS.

    :rtype: str
    :returns: version hash returned from VCS (git)
    """

    try:
        cmd = '/usr/bin/git', 'rev-parse', 'HEAD'
        pipe = subprocess.PIPE
        process = subprocess.Popen(cmd, stdout=pipe, stderr=pipe, cwd=settings.BASE_DIR)
        stdout, stderr = process.communicate()

        if (process.returncode != 0) or (not stdout.strip()) or stderr.strip():  # pragma: no cover
            return '(ERROR)'
        else:
            return stdout.strip()[:12]

    except:  # pragma: no cover
        return '(UNKNOWN)'
