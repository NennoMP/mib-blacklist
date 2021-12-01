from flask import request, jsonify

from mib.dao.blacklist_manager import BlacklistManager
from mib.models.blacklist import Blacklist

def block(body):
    """This method allows the blocking of an user."""

    blocking_id = body['blocking_id']
    blocked_id = body['blocked_id']

    block_relation = Blacklist()
    block_relation.set_relationship(blocking_id, blocked_id)
    BlacklistManager.create(relation=block_relation)

    response_object = {
        'status': 'success',
        'message': 'Successfully blocked',
    }

    return jsonify(response_object), 200


def unblock(body):
    """This method allows the unblocking of an user."""

    blocking_id = body['blocking_id']
    blocked_id = body['blocked_id']

    block_relation = BlacklistManager.retrieve_relation(blocking_id, blocked_id)
    BlacklistManager.delete(relation=block_relation)

    response_object = {
        'status': 'success',
        'message': 'Successfully unblocked',
    }

    return jsonify(response_object), 200

#TODO: maybe we need another for querying if blocked
