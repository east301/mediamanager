from django.conf import settings
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mediamanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # apps.system
    url(r'^$', 'apps.system.views.base'),
    url(r'^version/$', 'apps.system.views.version'),
)


if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns += patterns('',
        url(r'^admin/', include(admin.site.urls)),
    )
