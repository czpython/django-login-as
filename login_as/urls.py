try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('login_as.views',
    url('^$', 'chooser', name='login-as-chooser'),
    url('^(.+?)/$', 'login', name='login-as-login'),
)
