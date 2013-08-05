Django Bootstrap Forms
======================

Django Bootstrap Forms provides several customizable form templates which output HTML markup using Twitter Bootstrap HTML tag and CSS class format. HTML documentation can be viewed here:
http://getbootstrap.com/css/#forms

Note: there is a Django library that provides similar functionality to this one: Django Crispy Forms. Unlike Django Crispy Forms, which uses a custom form filter written in Python, Django Bootstrap Forms is just a set of Django templates, which can be easily modified. 

### This project has two main goals:

1. To enable both client-side and server-side form validation, but To keep all the form validation rules in the Django Python code (DRY: no duplicate form validation logic has to be repeated in the JavaScript.): The validation logic only exits in the Django model and Django view. 

2. To give the front-end developer complete control over the form HTML; the HTML is completely editable within with the app's files: in the Django templates and in the Django ModelForms class in the view.

### Key files:

1. The templates
2. The sub-template
3. The model
4. The view

#### 1. Page template:


https://github.com/danny8000/django-bootstrap-forms/blob/master/dbf_project/django_bootstrap_forms/templates/django_bootstrap_forms/add_contact.html

#### 2. Partial Template:

https://github.com/danny8000/django-bootstrap-forms/blob/master/dbf_project/django_bootstrap_forms/templates/django_bootstrap_forms/partial/_input_form_bootstrap.html

The partial template contains all the presentation logic, and is where the front-end developer would make the HTML edits if needed. Currently

Parsley.js is used for client-side form validation using HTML 5 data attributes.

#### 3. Django Model:

#### 4. Django View (modelforms):


Note: The popular Django library for creating HTML 5 form elements, "Django Floppy Forms" is not compatible with the code in this repository. To create HTML 5 forms using this repo, you would edit the partial/_input_form_bootstrap.html Django template file.
