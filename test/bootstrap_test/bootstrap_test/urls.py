from django.conf.urls import patterns, include, url
from django.contrib import admin

from test_app.views import FormView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bootstrap_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('', FormView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
