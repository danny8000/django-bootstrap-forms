from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core import urlresolvers

class AuthMiddelware(object):
    def process_request(self, request):
        domainpath = request.META.get('PATH_INFO')
        print domainpath
        
        if domainpath.startswith('/django_bootstrap_forms_portal/'):
            # make sure they are signed in
            if not request.user.is_authenticated():
                login_url = urlresolvers.reverse('django_bootstrap_forms_login') + '?next=' + domainpath
                return HttpResponseRedirect(login_url)
                # return redirect('admin:index')
