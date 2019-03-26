# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

from rest_framework import routers
from api.views import MenuItemViewSet

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]

urlpatterns += [
    url(r'^admin/', admin.site.urls),  # NOQA
    url(r'^api/', include(router.urls)),
    url(r'^', include('cms.urls')),
]

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
