# Django OpenStax Accounts

`django-openstax-accounts` is a Django app to read data from the logged-in user's OpenStax account using the SSO cookie.

## Quick start

Add the following settings to your settings file:
```python
    # OpenStax Accounts settings
    SSO_COOKIE_NAME = "<oxa_env>"
    SSO_SIGNATURE_PUBLIC_KEY = "<public_key_for_accounts>"
    SSO_ENCRYPTION_PRIVATE_KEY = "<private_key_for_accounts>"
```

## Usage
If you need to access the current user's OpenStax account UUID, you can use the `get_logged_in_user_uuid` function from `openstax_accounts.functions`. This function will return a dictionary with the user's data.

```python
from django.shortcuts import render
from openstax_accounts.functions import get_logged_in_user_uuid

def my_view(request):
    user_uuid = get_logged_in_user_uuid(request)
    return render(request, "my_template.html", {"user_uuid": user_uuid})
```

## Releasing

The GitHub Actions workflow automatically publishes to PyPI when a tag is pushed.

1. Bump the version in `setup.cfg`
2. Commit and push the change
3. Create and push a tag:
   ```sh
   git tag v1.0.1
   git push origin v1.0.1
   ```
4. The workflow will build and publish the new version to PyPI automatically
