from django.conf.urls import patterns, url

urlpatterns = patterns('django_bootstrap_forms.views',
    url(r'^$', 'index', name='index'),
    url(r'^add_contact/$', 'add_contact', name='add_contact'),
    url(r'^edit_contact/(?P<contact_id>\d+)/$', 'edit_contact', name='edit_contact'),
    url(r'^delete/(?P<contact_id>\d+)/$', 'delete_contact', name='delete_contact'),
    url(r'^thanks/$', 'thanks', name='thanks'),
)
