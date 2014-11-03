from django.conf.urls import patterns, include, url
from VideoQuiz import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',
        'VideoQuiz.views.home',
        name='home'
    ),
    url(r'^validate/$',
        'VideoQuiz.views.Validate',
        name='validate'
    ),
    url(r'^started_watching/$',
        'VideoQuiz.views.StartedWatching',
        name='started-watching'
    ),
    url(r'^finished_watching/$',
        'VideoQuiz.views.FinishedWatching',
        name='finished-watching'),

    url(r'^ValidateQuiz/$',
        'VideoQuiz.views.quizcheck'),

    url(r'^SelectGift/$',
        'VideoQuiz.views.SelectGift',
        name='select-gift'),

    url(r'^ListStores/(?P<token>[0-9A-Z].+)/$',
        'VideoQuiz.views.ListStores',
        name='list-stores'),

    url(r'^SaveStoreSelection/$',
        'VideoQuiz.views.SaveStoreSelection',
        name='save-store-selection'),
    url(r'^PayItForward/$',
        'VideoQuiz.views.PayItForward',
        name='pay-it-forward'),
    url(r'^report/$',
        'VideoQuiz.views.CompletedReport'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
