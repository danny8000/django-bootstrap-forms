from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
# The next two lines do not work with SQL Lite:
#from django_extensions.db.fields import CreationDateTimeField
#from django_extensions.db.fields import ModificationDateTimeField


def validate_agree(value):
    if value != True:
        raise ValidationError(u'You must agree to our terms and conditions.')


STATE_CHOICES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(verbose_name="Email Address", help_text='Email address will be used as your username for login.')
    phone = models.CharField(
        max_length=12,
        blank=True,
        validators=[
            RegexValidator(
                r'^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$',
                'Must be a US phone number (xxx-xxx-xxxx).',
                'invalid_phone_number'
            ),
        ],

        help_text='XXX-XXX-XXXX'
    )
    state = models.CharField(max_length=2, choices=STATE_CHOICES, blank=True, help_text='Please choose a state.')
    password = models.CharField(
        max_length=16,
        validators=[
            RegexValidator(
                r'^(?=.*[^a-zA-Z])(?=.*[a-z])(?=.*[A-Z])\S{8,}$',
                'Password must contain one each of the following characters: uppercase, lowercase, number, and special character (!@#$%^&*). It must be 8-16 characters long. It may not contain spaces or any other special characters than those listed.',
                'invalid_password'
            ),
        ],
        help_text='Password must contain one each of the following characters: uppercase, lowercase, number, and special character (!@#$%^&*). It may not contain spaces or any other special characters than those listed.'
    )
    note = models.TextField(blank=True, help_text='Notes about this contact.')
    agree = models.BooleanField(null=False, blank=False, help_text='Do you agree to the site <a href="#">Terms and Conditions?</a>', validators=[validate_agree])

    created_by = models.ForeignKey(User, editable=False, blank=True, null=True, related_name='+')
    modified_by = models.ForeignKey(User, editable=False, blank=True, null=True, related_name='+')

    #created_date = CreationDateTimeField()
    #modified_date = ModificationDateTimeField()

    def __unicode__(self):  
        return self.first_name
