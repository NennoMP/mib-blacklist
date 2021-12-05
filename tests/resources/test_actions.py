from faker import Faker

from .view_test import ViewTest
from tests.models.test_blacklist import TestBlacklist


class TestActions(ViewTest):

    faker = Faker('it_IT')

    @classmethod
    def setUpClass(cls):
        super(TestActions, cls).setUpClass()

    # Block tests
    def test_block(self):

        # Block an already blocked user
        blacklist_relation = TestBlacklist.generate_random_relation()
        
        self.blacklist_manager.create_relation(blacklist_relation)
        
        data = {
            'blocking_id': blacklist_relation.id_user,
            'blocked_id': blacklist_relation.id_blocked,
        }

        response = self.client.put('/blacklist', json=data)
        json_response = response.json

        assert response.status_code == 409
        assert json_response["status"] == 'failed'
        assert json_response["message"] == 'You already blocked this user'

        # Successfully block a user
        blacklist_relation = TestBlacklist.generate_random_relation()

        data = {
            'blocking_id': blacklist_relation.id_user,
            'blocked_id': blacklist_relation.id_blocked,
        }

        response = self.client.put('/blacklist', json=data)
        json_response = response.json

        assert response.status_code == 200
        assert json_response["status"] == 'success'
        assert json_response["message"] == 'Successfully blocked'

    # Unblock tests
    def test_unblock(self):

        # Unblock an user that was not blocked
        blacklist_relation = TestBlacklist.generate_random_relation()

        self.blacklist_manager.create_relation(blacklist_relation)

        data = {
            'blocking_id': blacklist_relation.id_user,
            'blocked_id': blacklist_relation.id_blocked+1,
        }

        response = self.client.post('/blacklist', json=data)
        json_response = response.json

        assert response.status_code == 404
        assert json_response["status"] == 'failed'
        assert json_response["message"] == 'This user was not blocked'

        # Successfully unblock a user
        blacklist_relation = TestBlacklist.generate_random_relation()
        self.blacklist_manager.create_relation(blacklist_relation)

        data = {
            'blocking_id': blacklist_relation.id_user,
            'blocked_id': blacklist_relation.id_blocked,
        }

        response = self.client.post('/blacklist', json=data)
        json_response = response.json

        assert response.status_code == 200
        assert json_response["status"] == 'success'
        assert json_response["message"] == 'Successfully unblocked'

    # Get blocked users tests
    def test_get_blocked_user(self):
        blacklist_relation = TestBlacklist.generate_random_relation()
        self.blacklist_manager.create_relation(blacklist_relation)
        url = "/blocked_users/%s" % (blacklist_relation.id_user)
        response = self.client.get(url)
        json_response = response.json

        assert response.status_code == 200
        assert json_response["status"] == 'success'

