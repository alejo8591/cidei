from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cidei.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.index', name='index'),
    url(r'^items/$', 'app.views.items', name='Items'),
    url(r'^items/(?P<item_id>\d+)/$', 'app.views.items_details', name='details-item'),
    url(r'^items/add/$', 'app.views.add_item', name="add-items"),
    url(r'^category/$', 'app.views.categories', name='Categorys'),
    url(r'^category/(?P<slug>[\w-]+)/$', 'app.views.category_details', name='add-details'),
    url(r'^about/$', 'app.views.about', name='about'),
)
