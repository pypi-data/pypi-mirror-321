from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse
from environs import Env

from django_opalstack.models import Token

env = Env()
env.read_env()
OPAL_KEY = env.str("OPAL_KEY")
SERVER_ID = env.str("SERVER_ID")
USER_ID = env.str("USER_ID")
USER_NAME = env.str("USER_NAME")
APP_ID = env.str("APP_ID")


@override_settings(DEBUG=False)
class OpalstackViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_superuser("boss", "test@example.com", "p4s5w0r6")
        User.objects.create_superuser("impostor", "impostor@example.com", "p4s5w0r6")
        Token.objects.create(
            name="test_token",
            key=OPAL_KEY,
            user=user,
        )

    def test_unlogged_status_code(self):
        response = self.client.get(
            reverse(
                "django_opalstack:token_list",
            )
        )
        self.assertEqual(response.status_code, 302)
        token = Token.objects.get(name="test_token")
        response = self.client.get(
            reverse(
                "django_opalstack:token_detail",
                kwargs={"pk": token.id},
            )
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(
            reverse(
                "django_opalstack:user_list",
                kwargs={"pk": token.id},
            )
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(
            reverse(
                "django_opalstack:app_list",
                kwargs={"pk": token.id},
            )
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(
            reverse(
                "django_opalstack:site_list",
                kwargs={"pk": token.id},
            )
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(
            reverse(
                "django_opalstack:app_detail",
                kwargs={"pk": token.id},
            )
        )
        self.assertEqual(response.status_code, 302)

    def test_impostor_login_status_code(self):
        self.client.login(username="impostor", password="p4s5w0r6")
        response = self.client.get(
            reverse(
                "django_opalstack:token_list",
            )
        )
        self.assertEqual(response.status_code, 200)
        # test that queryset is empty
        self.assertFalse(response.context["object_list"].exists())
        token = Token.objects.get(name="test_token")
        response = self.client.get(
            reverse(
                "django_opalstack:token_detail",
                kwargs={"pk": token.id},
            )
        )
        self.assertEqual(response.status_code, 403)
        response = self.client.get(
            reverse(
                "django_opalstack:user_list",
                kwargs={"pk": token.id},
            )
        )
        self.assertEqual(response.status_code, 403)
        response = self.client.get(
            reverse(
                "django_opalstack:app_list",
                kwargs={"pk": token.id},
            )
        )
        self.assertEqual(response.status_code, 403)
        response = self.client.get(
            reverse(
                "django_opalstack:site_list",
                kwargs={"pk": token.id},
            )
        )
        self.assertEqual(response.status_code, 403)
        response = self.client.get(
            reverse(
                "django_opalstack:app_detail",
                kwargs={"pk": token.id},
            )
        )
        self.assertEqual(response.status_code, 403)

    def test_boss_login_token_list_view(self):
        self.client.login(username="boss", password="p4s5w0r6")
        response = self.client.get(
            reverse(
                "django_opalstack:token_list",
            )
        )
        # test status code
        self.assertEqual(response.status_code, 200)
        # test that queryset is empty
        self.assertTrue(response.context["object_list"].exists())
        # test template
        self.assertTemplateUsed(response, "django_opalstack/token_list.html")
        response = self.client.get(
            reverse(
                "django_opalstack:token_list",
            ),
            headers={"Hx-Request": "true"},
        )
        # test htmx template
        self.assertTemplateUsed(response, "django_opalstack/htmx/token_list.html")

    def test_boss_login_token_detail_view(self):
        self.client.login(username="boss", password="p4s5w0r6")
        token = Token.objects.get(name="test_token")
        response = self.client.get(
            reverse(
                "django_opalstack:token_detail",
                kwargs={"pk": token.id},
            )
        )
        # test status code
        self.assertEqual(response.status_code, 200)
        # test template
        self.assertTemplateUsed(response, "django_opalstack/token_detail.html")
        response = self.client.get(
            reverse(
                "django_opalstack:token_detail",
                kwargs={"pk": token.id},
            ),
            headers={"Hx-Request": "true"},
        )
        # test htmx template
        self.assertTemplateUsed(response, "django_opalstack/htmx/token_detail.html")
        # test context
        self.assertTrue("web_servers" in response.context)

    def test_boss_login_user_list_view(self):
        self.client.login(username="boss", password="p4s5w0r6")
        token = Token.objects.get(name="test_token")
        response = self.client.get(
            reverse(
                "django_opalstack:user_list",
                kwargs={"pk": token.id},
            ),
            headers={"Hx-Request": "true"},
        )
        # test status code no server id
        self.assertEqual(response.status_code, 404)
        response = self.client.get(
            reverse(
                "django_opalstack:user_list",
                kwargs={"pk": token.id},
            )
            + f"?server_id={SERVER_ID}",
        )
        # test status code no htmx
        self.assertEqual(response.status_code, 404)
        response = self.client.get(
            reverse(
                "django_opalstack:user_list",
                kwargs={"pk": token.id},
            )
            + f"?server_id={SERVER_ID}",
            headers={"Hx-Request": "true"},
        )
        # test status code
        self.assertEqual(response.status_code, 200)
        # test htmx template
        self.assertTemplateUsed(response, "django_opalstack/htmx/user_list.html")
        # test context
        self.assertTrue("osusers" in response.context)

    def test_boss_login_app_list_view(self):
        self.client.login(username="boss", password="p4s5w0r6")
        token = Token.objects.get(name="test_token")
        response = self.client.get(
            reverse(
                "django_opalstack:app_list",
                kwargs={"pk": token.id},
            ),
            headers={"Hx-Request": "true"},
        )
        # test status code no osuser name
        self.assertEqual(response.status_code, 404)
        response = self.client.get(
            reverse(
                "django_opalstack:app_list",
                kwargs={"pk": token.id},
            )
            + f"?server_id={SERVER_ID}&osuser_name={USER_NAME}",
        )
        # test status code no htmx
        self.assertEqual(response.status_code, 404)
        response = self.client.get(
            reverse(
                "django_opalstack:app_list",
                kwargs={"pk": token.id},
            )
            + f"?server_id={SERVER_ID}&osuser_name={USER_NAME}",
            headers={"Hx-Request": "true"},
        )
        # test status code
        self.assertEqual(response.status_code, 200)
        # test htmx template
        self.assertTemplateUsed(response, "django_opalstack/htmx/app_list.html")
        # test context
        self.assertTrue("apps" in response.context)

    def test_boss_login_site_list_view(self):
        self.client.login(username="boss", password="p4s5w0r6")
        token = Token.objects.get(name="test_token")
        response = self.client.get(
            reverse(
                "django_opalstack:site_list",
                kwargs={"pk": token.id},
            ),
            headers={"Hx-Request": "true"},
        )
        # test status code no server id
        self.assertEqual(response.status_code, 404)
        response = self.client.get(
            reverse(
                "django_opalstack:site_list",
                kwargs={"pk": token.id},
            )
            + f"?server_id={SERVER_ID}",
        )
        # test status code no htmx
        self.assertEqual(response.status_code, 404)
        response = self.client.get(
            reverse(
                "django_opalstack:site_list",
                kwargs={"pk": token.id},
            )
            + f"?server_id={SERVER_ID}",
            headers={"Hx-Request": "true"},
        )
        # test status code
        self.assertEqual(response.status_code, 200)
        # test htmx template
        self.assertTemplateUsed(response, "django_opalstack/htmx/site_list.html")
        # test context
        self.assertTrue("opal_sites" in response.context)

    def test_boss_login_domain_list_view(self):
        self.client.login(username="boss", password="p4s5w0r6")
        token = Token.objects.get(name="test_token")
        response = self.client.get(
            reverse(
                "django_opalstack:domain_list",
                kwargs={"pk": token.id},
            ),
        )
        # test status code no htmx
        self.assertEqual(response.status_code, 404)
        response = self.client.get(
            reverse(
                "django_opalstack:domain_list",
                kwargs={"pk": token.id},
            ),
            headers={"Hx-Request": "true"},
        )
        # test status code
        self.assertEqual(response.status_code, 200)
        # test htmx template
        self.assertTemplateUsed(response, "django_opalstack/htmx/domain_list.html")
        # test context
        self.assertTrue("domains" in response.context)

    def test_boss_login_app_detail_view(self):
        self.client.login(username="boss", password="p4s5w0r6")
        token = Token.objects.get(name="test_token")
        response = self.client.get(
            reverse(
                "django_opalstack:app_detail",
                kwargs={"pk": token.id},
            ),
            headers={"Hx-Request": "true"},
        )
        # test status code no app id
        self.assertEqual(response.status_code, 404)
        response = self.client.get(
            reverse(
                "django_opalstack:app_detail",
                kwargs={"pk": token.id},
            )
            + f"?app_id={APP_ID}",
        )
        # test status code no htmx
        self.assertEqual(response.status_code, 404)
        response = self.client.get(
            reverse(
                "django_opalstack:app_detail",
                kwargs={"pk": token.id},
            )
            + f"?app_id={APP_ID}",
            headers={"Hx-Request": "true"},
        )
        # test status code
        self.assertEqual(response.status_code, 200)
        # test htmx template
        self.assertTemplateUsed(response, "django_opalstack/htmx/app_detail.html")
        # test context
        self.assertTrue("app" in response.context)
