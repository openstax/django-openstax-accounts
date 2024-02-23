# Django OpenStax Accounts

`django-openstax-accounts` is a Django app to read data from the logged-in user's OpenStax account using the SSO cookie.

## Quick start

Add "openstax_accounts" to your INSTALLED_APPS setting like this:
```
    INSTALLED_APPS = [
        ...,
        "openstax_accounts",
    ]
```

Add the following settings to your settings file:
```
    # OpenStax Accounts settings
    SSO_COOKIE_NAME = "<oxa_env>"
    SSO_SIGNATURE_PUBLIC_KEY = "<public_key_for_accounts>"
    SSO_ENCRYPTION_PRIVATE_KEY = "<private_key_for_accounts>"
```

## Usage
If you need to access the user's OpenStax account data, you can use the `get_user_data` function from `openstax_accounts.utils`. This function will return a dictionary with the user's data.

```python
from django.shortcuts import render
from openstax_accounts.functions import get_logged_in_user_uuid

def my_view(request):
    user_uuid = get_logged_in_user_uuid(request)
    return render(request, "my_template.html", {"user_uuid": user_uuid})
```


