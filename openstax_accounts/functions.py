import logging

import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from django.conf import settings
from .strategy_2 import Strategy2

logger = logging.getLogger(__name__)

REQUEST_TIMEOUT = 30


def decrypt_cookie(cookie):
    strategy = Strategy2(
        signature_public_key=settings.SSO_SIGNATURE_PUBLIC_KEY,
        encryption_private_key=settings.SSO_ENCRYPTION_PRIVATE_KEY
    )
    return strategy.decrypt(cookie)


def get_logged_in_user_id(request):
    payload = decrypt_cookie(request.COOKIES.get(settings.SSO_COOKIE_NAME))
    return payload.user_id if payload else None


def get_logged_in_user_uuid(request):
    payload = decrypt_cookie(request.COOKIES.get(settings.SSO_COOKIE_NAME))
    return payload.user_uuid if payload else None


def get_token():
    client = BackendApplicationClient(client_id=settings.SOCIAL_AUTH_OPENSTAX_KEY)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(
        token_url=settings.ACCESS_TOKEN_URL,
        client_id=settings.SOCIAL_AUTH_OPENSTAX_KEY,
        client_secret=settings.SOCIAL_AUTH_OPENSTAX_SECRET,
    )
    return token


def _query_accounts_api(query):
    token = get_token()
    url = settings.USERS_QUERY + query
    response = requests.get(
        url,
        headers={"Authorization": f"Bearer {token['access_token']}"},
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    return _parse_user_data(response.json())


def get_user_info(uid=None):
    if not uid:
        return None
    return _query_accounts_api(f"q=id:{uid}")


def get_user_info_by_uuid(uuid=None):
    if not uuid:
        return None
    return _query_accounts_api(f"q=uuid:{uuid}")


def _parse_user_data(data):
    try:
        user_data = dict(data['items'][0])
    except (IndexError, KeyError):
        return None

    try:
        contact_infos = user_data['contact_infos']
        most_recent_email = max(contact_infos, key=lambda x: x['id'])
        user_data['email'] = most_recent_email['value']
    except (ValueError, IndexError, KeyError):
        user_data['email'] = None

    return user_data
