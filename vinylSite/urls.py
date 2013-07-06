from django.conf.urls import patterns, url

urlpatterns = patterns('vinylSite.views',
    url(r"^$", "home", name="home"),
)
"""
    url(r'^about_us/','about_us', name='about_us'),
	url(r'^products/','products', name='products'),
	url(r'^contact/','contact', name='contact'),
)
"""
