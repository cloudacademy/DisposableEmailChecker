DisposableEmailChecker
======================

Python class to detect Disposable Emails. Checks each email against a blacklist of ~890 domains used by various disposable email services.


Installation
------------

It's an ordinary Python package, just install via ``pip``::
    
    $ git clone git@github.com:cloudacademy/DisposableEmailChecker.git
    $ pip install ./DisposableEmailChecker
    
Download the example disposable email domains list or create your own and update ``settings.py``::

    $ cd /usr/share/
    $ wget https://raw.github.com/cloudacademy/DisposableEmailChecker/master/disposable_email_domains.txt
    

Usage
--------

To use the checker in your own scripts::

    >>> from disposable_email_checker import DisposableEmailChecker
    
    >>> email_checker = DisposableEmailChecker("/usr/share/disposable_email_domains.txt")
    >>> email_checker.is_disposable("foo@guerrillamail.com")
    True


Using with Django
-----------------

Add the following setting to your Django ``settings.py``::

    DISPOSABLE_EMAIL_DOMAINS = "/usr/share/disposable_email_domains.txt"
    
    
To use the checker during form validation, normally in ``forms.py``::

    from django import forms
    from django.utils.translation import ugettext_lazy as _
    from disposable_email_checker import DisposableEmailChecker
    
    
    class MyForm(forms.Form):
        email = forms.EmailField(label=_('Email'))
    
        def clean_email(self):
            email_checker = DisposableEmailChecker(settings.DISPOSABLE_EMAIL_DOMAINS)
            if email_checker.is_disposable(email):
                raise forms.ValidationError(_('Please use a different email address provider.'))
    
            return email


License
-------

Based on https://github.com/aaronbassett/DisposableEmailChecker
MIT: http://aaron.mit-license.org
