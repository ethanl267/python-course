from rest_api_2.models.user import UserModel
# from models.user import UserModel
from rest_api_2.tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('test', "abcd")

        self.assertEqual(user, username, 'test',)
        self.assertEqual(user, password, 'abcd',)
