Django Contact Widget
====================================

.. image:: https://img.shields.io/badge/license-MIT-blue.svg?maxAge=2592000
   :target: https://raw.githubusercontent.com/agusmakmun/django-contact-widget/master/LICENSE

.. image:: https://img.shields.io/pypi/pyversions/Django.svg?maxAge=2592000
   :target: https://github.com/agusmakmun/django-contact-widget

A simple contact form widget for Django.

.. image:: http://i.imgur.com/2dzKO2s.png


Install
----------------------

Django Contact Widget is available directly from `PyPI`_:

::

    $ pip install django-contact-widget


***).** And don't forget to add ``contact_widget`` to your ``INSTALLED_APPS``.


Requirement
----------------------

* ``Django>=1.10.1``


Database Migration
----------------------

::

    $ ./manage.py makemigrations contact_widget
    $ ./manage.py migrate contact_widget


Setting Configuration
----------------------

Email Configuration in file of ``settings.py``

::

    EMAIL_HOST = 'smtp.gmail.com'  # eg: 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'your_email@domain.com'
    EMAIL_HOST_PASSWORD = 'your_password'
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


URL configuration
----------------------

The easiest way to set up the views in ``django-contact-widget`` is to just use the provided ``URLconf``, found at ``contact_widget.urls``.
You can include it wherever you like in your site's URL configuration; for example, to have it live at the URL ``/contact/``:

::

    from django.conf.urls import include, url

    urlpatterns = [
        # ....
        url(r'^contact/', include('contact_widget.urls')),
    ]


Usage
----------------------

Include the template from ``contact_widget/contact.html`` to your sidebar for example.

::

    {% include "contact_widget/contact.html" %}



License
----------------------

- `MIT`_


.. _PyPI: https://pypi.python.org/pypi/django-contact-widget
.. _MIT: https://github.com/agusmakmun/django-contact-widget/blob/master/LICENSE
