from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^add_page/(?P<category_name_slug>[\w-]+)/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w-]+)/$', views.category, name='category'),
    url(r'^contact/$', views.contact_us, name='contact_us'),
    url(r'^register/$', views.register, name='register'),
)
