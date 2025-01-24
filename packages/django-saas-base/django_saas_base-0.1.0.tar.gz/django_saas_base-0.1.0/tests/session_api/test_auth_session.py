import re
from django.core import mail
from django.test import override_settings
from saas_base.models import UserEmail
from tests.client import FixturesTestCase


class TestSignUpAPI(FixturesTestCase):
    user_id = FixturesTestCase.ADMIN_USER_ID

    def test_signup_success(self):
        data1 = {"username": "demo", "email": "hi@foo.com", "password": "hello world"}
        resp = self.client.post("/s/signup/code", data=data1)
        self.assertEqual(resp.status_code, 204)
        self.assertEqual(len(mail.outbox), 1)
        msg = mail.outbox[0]
        codes = re.findall(r'Code: (\w{6})', msg.body)
        data2 = {**data1, "code": codes[0]}
        resp = self.client.post("/s/signup/confirm", data=data2)
        self.assertEqual(resp.status_code, 200)

    def test_signup_existed_email(self):
        user = self.get_user()
        UserEmail.objects.create(user=user, email="hi@foo.com", primary=True, verified=True)
        data = {"username": "foo", "email": "hi@foo.com", "password": "hello world"}
        resp = self.client.post("/s/signup/code", data=data)
        self.assertEqual(resp.status_code, 400)
        self.assertIn('existing', resp.json()['email'][0])

    def test_signup_blocked_email(self):
        rules = [
            {
                'backend': 'saas_base.security.rules.BlockedEmailDomains',
                'options': {
                    'domains': ['bar.com']
                }
            }
        ]
        with override_settings(SAAS={"SIGNUP_SECURITY_RULES": rules}):
            data = {"username": "bar", "email": "hi@bar.com", "password": "hello world"}
            resp = self.client.post("/s/signup/code", data=data)
            self.assertEqual(resp.status_code, 400)

    def test_signup_too_many_dots(self):
        rules = [{'backend': 'saas_base.security.rules.TooManyDots'}]
        with override_settings(SAAS={"SIGNUP_SECURITY_RULES": rules}):
            data = {"username": "bar", "email": "a.b.c.d.e.f@bar.com", "password": "hello world"}
            resp = self.client.post("/s/signup/code", data=data)
            self.assertEqual(resp.status_code, 400)

    def test_signup_turnstile(self):
        rules = [{'backend': 'saas_base.security.rules.Turnstile'}]
        with override_settings(SAAS={"SIGNUP_SECURITY_RULES": rules}):
            data = {"username": "bar", "email": "hi@bar.com", "password": "hello world"}
            resp = self.client.post("/s/signup/code", data=data)
            self.assertEqual(resp.status_code, 400)

            data = {**data, 'cf-turnstile-response': '**token**'}
            with self.mock_requests('turnstile_success.json'):
                resp = self.client.post("/s/signup/code", data=data)
                self.assertEqual(resp.status_code, 204)

            data = {**data, 'cf-turnstile-response': '**token**'}
            with self.mock_requests('turnstile_failed.json'):
                resp = self.client.post("/s/signup/code", data=data)
                self.assertEqual(resp.status_code, 400)


class TestLoginAPI(FixturesTestCase):
    user_id = FixturesTestCase.OWNER_USER_ID

    def test_login_with_username(self):
        user = self.get_user()

        data = {"username": user.username, "password": "hello world"}
        resp = self.client.post("/s/login", data=data)
        self.assertEqual(resp.status_code, 400)

        user.set_password('hello world')
        user.save()

        resp = self.client.post("/s/login", data=data)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("next", resp.json())

    def test_login_with_email(self):
        user = self.get_user()

        data = {"username": "hi@foo.com", "password": "hello world"}
        resp = self.client.post("/s/login", data=data)
        self.assertEqual(resp.status_code, 400)

        user.set_password('hello world')
        user.save()

        obj = UserEmail.objects.create(user=user, email="hi@foo.com")
        resp = self.client.post("/s/login", data=data)
        self.assertEqual(resp.status_code, 400)

        obj.primary = True
        obj.verified = True
        obj.save()

        resp = self.client.post("/s/login", data=data)
        self.assertEqual(resp.status_code, 200)
