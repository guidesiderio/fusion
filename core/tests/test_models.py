import uuid
from django.test import TestCase
from model_mommy import mommy
from core.models import get_file_path


class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f"{uuid.uuid4()}.png"

    def test_get_file_path(self):
        file = get_file_path(None, "test.png")
        self.assertTrue(len(file), len(self.filename))


class ServiceTestCase(TestCase):

    def setUp(self):
        self.service = mommy.make("Service")

    def test_str(self):
        self.assertEqual(str(self.service), self.service.title)


class RoleTestCase(TestCase):

    def setUp(self):
        self.role = mommy.make("Role")

    def test_str(self):
        self.assertEqual(str(self.role), self.role.name)


class TeamMemberTestCase(TestCase):

    def setUp(self):
        self.team_member = mommy.make("TeamMember")

    def test_str(self):
        self.assertEqual(str(self.team_member), self.team_member.name)
