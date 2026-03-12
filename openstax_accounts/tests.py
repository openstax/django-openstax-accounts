from django.test import TestCase, SimpleTestCase, Client
from http import cookies

from openstax_accounts.functions import decrypt_cookie, get_logged_in_user_uuid, get_logged_in_user_id


class DecryptCookieTestCase(SimpleTestCase):
    def setUp(self):
        self.sso_cookie = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..wdZ6RqqvBB00Lkir.9hfYiZy-iSjtmp1pkL9nfAcZCTxTUYO5D9PC4DXqxpbMhfsZQQOznO1pM9eoEbpswZF9DdL18vgh9beCIF5WwhHoQ5joZ_tax4fgcbPi_ifI35eraOaJA3qGX_Y616ThMr2GWneXPwfzPIyajK1kxw7NhAaLGFuGkD8G4863fLoF0ZYBnRb34HNtWOnVMDDn_vf1EiVhUp8F92G9hbZfQ4Yopt8YnkwqsvPayupf_C2shMiYM1bbZA5rAQ0ZKf9LaAufPOxb_cwk9TWfoi1sN7lZfFCA67-q4jENle81qaAeUo33nKuj4458HawlFeTK0W-jBPV1iSn_ohargvoMEYEOKXELCVh73j78h0og_FHfbUHZz-VyY4lIkaQhAJk0BPnIs10yZ6NMmVMSpuuhMRSKCZ4dbTVhL89xPfLaG3SPCrFZw7aUs7PMWpjBHu6O7MIiJN0OLTBVPetGxKZyUqVl-XwiyQvp3xOiUCNQd6eTcPz4X4svLNMGV6iJzSJKQPzAijw2In15aiyATRreTz_-KPnrRi-hFAzILCx2CauYvQ9oQOal-pbAe9oGkxDstSBcHeST7dIU3yKbPQnZSn1M00gxaxFxkd1ElwwRpN_CAUdE02N7IXrfIMk-0V3yUX2A_9sW-dKeQPrHDnT2JeeE9C8LC1qYBNatjAIaA-CylCrwVaX3QH9opHcMbrVXnndUG2enqqMz5YuUo6oAp3FXtK8tuho_jO6bkfi-tDx45X22adx58hDncNvNF0Pmxw1PybJrp1k.Rq5dqLkS-wUkCVUytlKyAw"

    def test_can_decrypt_sso_cookie(self):
        decrypted_cookie = decrypt_cookie(self.sso_cookie)
        self.assertEqual(decrypted_cookie.user_uuid, '467cea6c-8159-40b1-90f1-e9b0dc26344c')
        self.assertEqual(decrypted_cookie.user_id, 12345)
        self.assertEqual(decrypted_cookie.name, 'Test User')

    def test_missing_cookie_returns_none(self):
        self.assertIsNone(decrypt_cookie(None))
        self.assertIsNone(decrypt_cookie(''))

    def test_invalid_cookie_returns_none(self):
        self.assertIsNone(decrypt_cookie('not-a-valid-cookie'))


class LoggedInUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.sso_cookie = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..wdZ6RqqvBB00Lkir.9hfYiZy-iSjtmp1pkL9nfAcZCTxTUYO5D9PC4DXqxpbMhfsZQQOznO1pM9eoEbpswZF9DdL18vgh9beCIF5WwhHoQ5joZ_tax4fgcbPi_ifI35eraOaJA3qGX_Y616ThMr2GWneXPwfzPIyajK1kxw7NhAaLGFuGkD8G4863fLoF0ZYBnRb34HNtWOnVMDDn_vf1EiVhUp8F92G9hbZfQ4Yopt8YnkwqsvPayupf_C2shMiYM1bbZA5rAQ0ZKf9LaAufPOxb_cwk9TWfoi1sN7lZfFCA67-q4jENle81qaAeUo33nKuj4458HawlFeTK0W-jBPV1iSn_ohargvoMEYEOKXELCVh73j78h0og_FHfbUHZz-VyY4lIkaQhAJk0BPnIs10yZ6NMmVMSpuuhMRSKCZ4dbTVhL89xPfLaG3SPCrFZw7aUs7PMWpjBHu6O7MIiJN0OLTBVPetGxKZyUqVl-XwiyQvp3xOiUCNQd6eTcPz4X4svLNMGV6iJzSJKQPzAijw2In15aiyATRreTz_-KPnrRi-hFAzILCx2CauYvQ9oQOal-pbAe9oGkxDstSBcHeST7dIU3yKbPQnZSn1M00gxaxFxkd1ElwwRpN_CAUdE02N7IXrfIMk-0V3yUX2A_9sW-dKeQPrHDnT2JeeE9C8LC1qYBNatjAIaA-CylCrwVaX3QH9opHcMbrVXnndUG2enqqMz5YuUo6oAp3FXtK8tuho_jO6bkfi-tDx45X22adx58hDncNvNF0Pmxw1PybJrp1k.Rq5dqLkS-wUkCVUytlKyAw"

    def test_can_get_logged_in_user_uuid(self):
        biscuits = cookies.SimpleCookie()
        biscuits['oxa'] = self.sso_cookie
        self.client.cookies = biscuits
        response = self.client.get('/')
        request = response.wsgi_request
        uuid = get_logged_in_user_uuid(request)
        self.assertEqual(uuid, '467cea6c-8159-40b1-90f1-e9b0dc26344c')

    def test_can_get_logged_in_user_id(self):
        biscuits = cookies.SimpleCookie()
        biscuits['oxa'] = self.sso_cookie
        self.client.cookies = biscuits
        response = self.client.get('/')
        request = response.wsgi_request
        user_id = get_logged_in_user_id(request)
        self.assertEqual(user_id, 12345)

    def test_missing_cookie_returns_none(self):
        response = self.client.get('/')
        request = response.wsgi_request
        self.assertIsNone(get_logged_in_user_uuid(request))
