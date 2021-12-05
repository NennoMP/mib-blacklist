from .dao_test import DaoTest


class TestBlacklistManager(DaoTest):
    """Tests for the BlacklistManager methods."""

    @classmethod
    def setUpClass(cls):
        super(TestBlacklistManager, cls).setUpClass()
        from tests.models.test_blacklist import TestBlacklist
        cls.test_blacklist = TestBlacklist
        from mib.dao import blacklist_manager
        cls.blacklist_manager = blacklist_manager.BlacklistManager

    # Tests crud
    def test_crud(self):
        for _ in range(0, 10):
            blacklist_relation = self.test_blacklist.generate_random_relation()
            self.blacklist_manager.create_relation(relation=blacklist_relation)
            self.blacklist_manager.delete_relation(relation=blacklist_relation)
            