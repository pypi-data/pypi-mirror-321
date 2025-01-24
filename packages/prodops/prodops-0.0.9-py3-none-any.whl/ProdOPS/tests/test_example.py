"""
ProdOPS Test
"""

# Django
from django.test import TestCase


class TestProdOPS(TestCase):
    """
    TestProdOPS
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Test setup
        :return:
        :rtype:
        """

        super().setUpClass()

    def test_ProdOPS(self):
        """
        Dummy test function
        :return:
        :rtype:
        """

        self.assertEqual(True, True)
