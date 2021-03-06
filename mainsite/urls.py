from django.conf.urls import patterns, include, url
from django.contrib import admin
from sms.views import russms, receive, smsru, smsintel, websms

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mainsite.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', include(admin.site.urls)),
                       url(r'^russms/$', russms),
                       url(r'^smsru/$', smsru),
                       url(r'^websms/$', websms),
                       url(r'^smsintel/$', smsintel),
                       url(r'^receive/$', receive)
)