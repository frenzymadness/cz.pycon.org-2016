from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView


prefixed_urlpatterns = [
    url(r'^proposals/workshops$', RedirectView.as_view(url='/2016/proposals/talks')),
    url(r'^proposals/', include('pyconcz_2016.proposals.urls')),

    # static pages
    url(r'^$',
        TemplateView.as_view(template_name='pages/homepage.html'),
        name='homepage'),
    url(r'^about$',
        TemplateView.as_view(template_name='pages/about.html'),
        name='about'),
    url(r'^about/code$',
        TemplateView.as_view(template_name='pages/code.html'),
        name='about_code'),
    url(r'^about/team$',
        TemplateView.as_view(template_name='pages/team.html'),
        name='about_team'),
    url(r'^sponsors/offer$',
        TemplateView.as_view(template_name='pages/sponsors_offer.html'),
        name='sponsors_offer'),
]

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + [
    url(r'^2016/', include(prefixed_urlpatterns)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/2016/'))
]
