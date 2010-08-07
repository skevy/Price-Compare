from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'pricecompare.views.index'),
    (r'^groups/(?P<id>\d+)/$', 'pricecompare.views.detail'),
    (r'^viewall/$', 'pricecompare.views.viewall'),
    (r'^csv/((?P<id>\d+)/)?$', 'pricecompare.views.write_csv'),
    (r'^update/$', 'pricecompare.views.update'),
    (r'^admin/', include(admin.site.urls)),
)

# urlpatterns+= patterns('',
#     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
# )