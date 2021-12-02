from operator import and_
from mib.models.blacklist import Blacklist
from mib.dao.manager import Manager

from mib import db

class BlacklistManager(Manager):

    @staticmethod
    def create_relation(relation: Blacklist):
        Manager.create(relation=relation)

    def delete_relation(relation: Blacklist):
        Manager.delete(relation=relation)

    def retrieve_relation(blocking_id: int, blocked_id: int):
        Manager.check_none(blocking_id=blocking_id)
        Manager.check_none(blocked_id=blocked_id)

        return Blacklist.query.filter(and_(
            Blacklist.id_user == blocking_id,
            Blacklist.id_blocked == blocked_id)
        ).first()

    def retrieve_relationships(user_id: int):
        Manager.check_none(user_id=user_id)

        blocked_users = [r.id_blocked for r in db.session.query(Blacklist.id_blocked).filter(Blacklist.id_user == user_id)]

        return blocked_users