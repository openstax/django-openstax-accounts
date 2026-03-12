import logging

from joserfc import jwe, jwt
from joserfc.jwk import OctKey, RSAKey

logger = logging.getLogger(__name__)


class Strategy2:
    def __init__(self, signature_public_key, encryption_private_key):
        self.signature_public_key = signature_public_key
        self.encryption_private_key = encryption_private_key

    def decrypt(self, cookie):
        # Decoding is the reverse of what Accounts does to encode a cookie:
        # Accounts first signs the payload w/ the signature private key, then
        # it next symmetric encrypts that result w/ the encryption private key.

        if not cookie:
            return None

        try:
            enc_key = OctKey.import_key(self.encryption_private_key.encode())
            jwe_obj = jwe.decrypt_compact(cookie, enc_key)

            sig_key = RSAKey.import_key(self.signature_public_key)
            jwt_obj = jwt.decode(jwe_obj.plaintext, sig_key)
            jwt.JWTClaimsRegistry(
                aud={"essential": True, "value": "OpenStax"}
            ).validate(jwt_obj.claims)

            return Payload(jwt_obj.claims)
        except Exception:
            logger.exception("Could not decrypt cookie")
            return None

class Payload:
    def __init__(self, payload_dict):
        self.payload_dict = payload_dict
        self.user_uuid = payload_dict['sub']['uuid']
        self.user_id = payload_dict['sub'].get('id')
        self.name = payload_dict['sub'].get('name')
