from django.conf.urls import patterns, include, url
from django.contrib import admin
from learn.views import LearnView#, RedeemView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'acu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^learn/', 'learn.views.learn', name='learn'),
    # url(r'^redeem/', RedeemView.as_view(), name='redeem'),
    # url(r'^thanks/', 'learn.views.thanks', name='thanks'),
)
