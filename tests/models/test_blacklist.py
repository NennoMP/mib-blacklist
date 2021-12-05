from random import randint

from .model_test import ModelTest


class TestBlacklist(ModelTest):
    """Tests for Blacklist table methods."""

    @classmethod
    def setUpClass(cls):
        super(TestBlacklist, cls).setUpClass()

        from mib.models import blacklist
        cls.blacklist = blacklist

    # Generate a random relationship to use in the tests
    def generate_random_relation():
        id_user = randint(0, 100)
        id_blocked= randint(101, 200)

        from mib.models import Blacklist
        blacklist_relation = Blacklist(
            id_user=id_user,
            id_blocked=id_blocked,
        )

        return blacklist_relation

    # Set relationship
    def test_set_relationship(self):
        blacklist_relation = TestBlacklist.generate_random_relation()

        id_user = randint(0, 10)
        id_blocked = randint(10, 20)
        blacklist_relation.set_relationship(id_user, id_blocked)

        self.assertEqual(id_user, blacklist_relation.id_user)
        self.assertEqual(id_blocked, blacklist_relation.id_blocked)
