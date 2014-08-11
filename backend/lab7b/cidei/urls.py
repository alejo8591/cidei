from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings

from rest_framework import routers

from accounts.views import UserViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'profile', UserProfileViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cidei.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('app.urls')),
    url(r'^accounts/', include('accounts.urls')),
)

if settings.DEBUG:
	urlpatterns+= patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root' : settings.MEDIA_ROOT}), 
	)	