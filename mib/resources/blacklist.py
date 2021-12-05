from flask import jsonify

from mib.models.blacklist import Blacklist
from mib.dao.blacklist_manager import BlacklistManager


def block(body):
    """
    This method allows the blocking of an user.
    
    :return: json response and status code
        - 201: successfully blocked
        - 409: user already blocked
    """

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
    """
    This method allows the unblocking of an user.
    
    :return: json response and status code
        - 200: successfully unblocked
        - 404: user was not blocked
    """

    blocking_id = body['blocking_id']
    blocked_id = body['blocked_id']

    block_relation = BlacklistManager.retrieve_relation(
                                                    blocking_id, 
                                                    blocked_id
                                                )
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
    """
    This method allows to retrieve the list of blocked users for a specific user.

    :return: json response and status code
        - 200: retrieved blocked users 
    """

    blocked_users = BlacklistManager.retrieve_relationships(user_id)
    response_object = {
        'status': 'success',
        'blocked_users': blocked_users,
    }

    return jsonify(response_object), 200
