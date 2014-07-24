from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('myblog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'myblog/login.html'}, name = 'auth_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'myblog/logout.html'}, name = 'auth_logout'),
    url (r'^ckeditor/', include('ckeditor.urls')),
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)