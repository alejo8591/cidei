from django.conf.urls import patterns, include, url
from accounts.views import UsernameViewSetOne

urlpatterns = patterns('',
	url(r'^register/$', 'accounts.views.register', name='register'),
	url(r'^login/$', 'accounts.views.user_login', name='login') ,
	url(r'^logout/$', 'accounts.views.user_logout', name='logout'),
	url(r'^usernames/(?P<username>[\w-]+)/$', UsernameViewSetOne.as_view()),
)