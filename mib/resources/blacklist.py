from flask import request, jsonify

from mib.dao.blacklist_manager import BlacklistManager
from mib.models.blacklist import Blacklist

def block(body):
    """This method allows the blocking of an user."""

    blocking_id = body['blocking_id']
    blocked_id = body['blocked_id']

    block_relation = BlacklistManager.retrieve_relation(
                                                blocking_id,
                                                blocked_id
                                            )
    if block_relation is None:
        block_relation = Blacklist()
        block_relation.id_blocked = blocked_id
        block_relation.id_user = blocking_id
        BlacklistManager.create(relation=block_relation)

        response_object = {
            'status': 'success',
            'message': 'Successfully blocked',
        }
        response_status_code = 200
    else:
        response_object = {
            'status': 'failed',
            'message': 'You already blocked this user',
        }
        response_status_code = 409


    return jsonify(response_object), response_status_code


def unblock(body):
    """This method allows the unblocking of an user."""

    blocking_id = body['blocking_id']
    blocked_id = body['blocked_id']

    block_relation = BlacklistManager.retrieve_relation(blocking_id, blocked_id)
    if block_relation is None:
        response_object = {
            'status': 'failed',
            'message': 'This user was not blocked',
        }
        response_status_code = 404
    else:
        BlacklistManager.delete(relation=block_relation)
        response_object = {
            'status': 'success',
            'message': 'Successfully unblocked',
        }
        response_status_code = 200

    return jsonify(response_object), response_status_code


def get_blocked_users(user_id: int):
    """This method allows to retrieve the list of blocked users for a specific user.
    """

    blocked_users = BlacklistManager.retrieve_relationships(user_id)

    response_object = {
        'status': 'success',
        'blocked_users': blocked_users,
    }

    return jsonify(response_object), 200
