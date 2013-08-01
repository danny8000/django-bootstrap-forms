Django Bootstrap Forms
======================

An alternative to Django Floppy Forms. Django Bootstrap Forms keeps the form HTML in the Django templates. 

### This project has two main goals:

1. To enable both client-side and server-side form validation, but To keep all the form validation rules in the Django Python code (DRY: no duplicate form validation logic has to be repeated in the JavaScript.): The validation logic only exits in the Django model and Django view. 
2. To give the front-end developer complete control over the form HTML; the HTML is completely editable within with the app's files: in the Django templates and in the Django ModelForms class in the view.

### Key files:

1. The templates
2. The sub-template
3. The model
4. The view

#### The templates


Parseley.js is used for client-side form validation.
