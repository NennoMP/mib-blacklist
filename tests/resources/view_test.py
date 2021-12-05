import unittest


class ViewTest(unittest.TestCase):
    """This class should be implemented by all classes that tests resources."""
    
    client = None

    @classmethod
    def setUpClass(cls):
        from mib import create_app
        app = create_app()
        cls.client = app.test_client()

        from tests.models.test_blacklist import TestBlacklist
        cls.test_user = TestBlacklist

        from mib.dao.blacklist_manager import BlacklistManager
        cls.blacklist_manager = BlacklistManager
