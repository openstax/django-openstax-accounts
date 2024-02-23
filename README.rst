========================
django-openstax-accounts
========================

``django-openstax-accounts`` is a Django app to read data
from the logged-in user's OpenStax account using the SSO cookie.

Quick start
-----------

Add the following settings to your settings file::

    # OpenStax Accounts settings
    SSO_COOKIE_NAME = "<oxa_env>"
    SSO_SIGNATURE_PUBLIC_KEY = "<public_key_for_accounts>"
    SSO_ENCRYPTION_PRIVATE_KEY = "<private_key_for_accounts>"


Usage
-----

If you need to access the current user's OpenStax account UUID,
you can use the ``get_logged_in_user_uuid`` function from ``openstax_accounts.functions``.
This function will a UUID.::

    from django.shortcuts import render
    from openstax_accounts.functions import get_logged_in_user_uuid

    def my_view(request):
        user_uuid = get_logged_in_user_uuid(request)
        # function to do something with the uuid, like save it to your database or use for an API call
        return render(request, "my_template.html", {"user_uuid": user_uuid})

