# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`django-openstax-accounts` is a reusable Django app (published to PyPI) that provides SSO cookie decryption and user info retrieval for OpenStax services. It has no models, views, or URLs — only utility functions.

## Build & Test Commands

```bash
# Build package
python3 -m build

# Run tests
python -m django test openstax_accounts --settings=openstax_accounts.tests

# Release: bump version in setup.cfg, commit, then tag
git tag v1.x.x && git push origin v1.x.x
```

CI/CD publishes to PyPI automatically on tag push via GitHub Actions.

## Architecture

**Two core modules:**

- `openstax_accounts/functions.py` — Public API. Provides `get_logged_in_user_uuid(request)`, `get_logged_in_user_id(request)`, `get_token()`, `get_user_info(uid)`, `get_user_info_by_uuid(uuid)`, and `retrieve_user_data(url)`. All read from Django settings and `request.COOKIES`.

- `openstax_accounts/strategy_2.py` — Decryption layer. Implements `Strategy2` class that decrypts JWE (A256GCM) then verifies JWT (RS256) from SSO cookies. Returns a `Payload` object with `user_uuid`, `user_id`, and `name`.

**Authentication flow:** SSO cookie → JWE decrypt (private key) → JWT verify (public key) → Payload object with user data.

**API flow:** OAuth2 client credentials → access token → query Accounts API → parse user data (email, name, role, faculty status, uuid, is_administrator).

## Required Django Settings

```python
SSO_COOKIE_NAME, SSO_SIGNATURE_PUBLIC_KEY, SSO_ENCRYPTION_PRIVATE_KEY
SOCIAL_AUTH_OPENSTAX_KEY, SOCIAL_AUTH_OPENSTAX_SECRET
USERS_QUERY, ACCESS_TOKEN_URL
```

## Dependencies

Django >= 3.0, PyJWE, PyJWT, requests-oauthlib. Python 3.8–3.12.
