# Create your views here.
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
#from django.forms.models import modelformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

#import json
from django_bootstrap_forms.models import Contact
import pprint

class ContactEditModelForm(forms.ModelForm):

    class Meta:
        model = Contact

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)

        # There are 4 field-level attributes:
        # 1. tag: (form tag, can only be one of: input, textarea, select)
        # 2. type: (html attribute, e.g.: checkbox, file, hidden, password, radio, text)
        # 3. attributes: other html field attributes (e.g.: size, rows, cols)
        # 4. css_class: Bootstrap class or other
        # 5. field_validators: Parsely.JS, can be more than one attribute, see http://parsleyjs.org/documentation.html#parsleyfield
        # 6. error_messages: custom error messages to replace the standard Django validation errors

        # tag = input is default
        self.fields['email'].tag = 'input'
        self.fields['email'].type = 'text'
        self.fields['email'].css_class = 'input-xlarge'
        self.fields['email'].field_validators = 'data-type = "email" data-trigger = "change"'
        # Over-ride the default error message:
        self.fields['email'].error_messages.update({'required': 'Please enter a valid email address.'})

        self.fields['first_name'].type = 'text'
        self.fields['first_name'].css_class = 'input-xlarge'
        self.fields['first_name'].field_validators = 'data-trigger = "change"'

        self.fields['last_name'].type = 'text'
        self.fields['last_name'].css_class = 'input-xlarge'
        self.fields['last_name'].field_validators = 'data-trigger = "change"'

        self.fields['phone'].type = 'text'
        self.fields['phone'].field_validators = 'data-type = "phone" data-trigger = "change"'

        self.fields['state'].tag = 'select'

        self.fields['password'].type = 'password'
        self.fields['password'].css_class = 'input-xlarge'
        self.fields['password'].field_validators = 'data-rangelength="[8,16]"'

        self.fields['note'].tag = 'textarea'
        self.fields['note'].attributes = 'rows="5"'
        self.fields['note'].css_class = 'input-xlarge'

        self.fields['agree'].type = 'checkbox'
        self.fields['agree'].field_validators = 'data-trigger = "change"'


def index(request):
    contact_list = Contact.objects.all()
    return render(request, 'django_bootstrap_forms/index.html', locals())


def thanks(request):
    #return render(request, 'django_bootstrap_forms/thanks.html', {'message': message})
    return render(request, 'django_bootstrap_forms/thanks.html')


def add_contact(request):
    if request.method == "POST":
        contact_form = ContactEditModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            #return HttpResponse('Contact updated')
            return HttpResponseRedirect('/django_bootstrap_forms/thanks/')
    # GET
    else:
        contact_form = ContactEditModelForm()

        # contact_form.fields is a SortedDict, so you need to loop through it to see the field contact as a string
        #print("Add Contact Fields:")
        #for key in contact_form.fields:
        #    print '\nkey:', key, '\ndict:'
        #    pprint.pprint(contact_form.fields[key].__dict__)

    return render(request, 'django_bootstrap_forms/add_contact.html', {'contact_form': contact_form})

#@login_required
#@user_passes_test(lambda u: u.has_perm('django_bootstrap_forms.delete_contact'), login_url='/accounts/login/')
def delete_contact(request, contact_id):

    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return HttpResponseRedirect(reverse('django_bootstrap_forms:index'))


#@login_required
#@user_passes_test(lambda u: u.has_perm('django_bootstrap_forms.change_contact'), login_url='/accounts/login/')
def edit_contact(request, contact_id):
    language =  'en-us'
    session_language = 'en-us'
    # the RESTful URL should always contact_id whether or not there is POST data, like this: modelform/1/
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == "POST":

        contact_form = ContactEditModelForm(request.POST, instance=contact)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponseRedirect(reverse('django_bootstrap_forms:index'))

    else:
        contact_form = ContactEditModelForm(instance=contact)

    return render(request, 'django_bootstrap_forms/edit_contact.html', {'contact': contact, 'contact_form': contact_form})
