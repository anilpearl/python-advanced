from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'MyCms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','MyCms.views.index', name='index'),
    url(r'^about/$','MyCms.views.about', name='about'),
    url(r'^info/$','MyCms.views.info', name='info'),
    url(r'^hello/$','MyCms.views.home', name='home'),
    url(r'^submit/$','MyCms.views.submit', name='submit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
