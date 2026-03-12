SECRET_KEY = "test-secret-key-not-for-production"

INSTALLED_APPS = [
    "openstax_accounts",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "openstax_accounts.test_urls"

SSO_COOKIE_NAME = "oxa"

SSO_SIGNATURE_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyz0gzC9Lg5mXdYu9Szic
s3VDuLTwVIUhTuSjBi78QqFTPUiT57vep6n88uQQG7E53Nm/LdAoIEoO5013dcDX
Xi+BZMcOPgihgpcJlR81alHS54K7ujQRWU6l+kAeVRi5Q+8HGAEy74rkjObndU++
wUQQGSDW4SQIlPtyhHyTuH/QzLaEZxovwKAGqxs0PpITnOkost99bXsbEc7hMUwt
BgSQztUeSspbCaHjOg/pNGgJ62EEG0Dc/kTXwflAhVZ5xOJNKPuEz3yiC/UcaOeZ
IGs7yfK5SoudNGAGoOoyVEKbqHoSipGuRNN8uPcOj2ykxDqtbQnwH28SCCab7LMP
fQIDAQAB
-----END PUBLIC KEY-----"""

SSO_ENCRYPTION_PRIVATE_KEY = 'a]gzHX2*E=N3T9dW5AF+bD&6$@q!r^e2'
