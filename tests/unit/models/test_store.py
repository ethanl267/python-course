from rest_api_2.models.store import StoreModel
from rest_api_2.tests.unit.unit_base_test import UnitBaseTest
from rest_api_2.unittest import TestCase

 
class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('test')

        self.assertEqual(store.name, 'test',"The name of the store creation does not equal the constructor argument.")