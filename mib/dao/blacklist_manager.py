from mib.models.blacklist import Blacklist
from mib.dao.manager import Manager

class BlacklistManager(Manager):

    @staticmethod
    def create_relation(relation:Blacklist):
        Manager.create(relation=relation)

    def delete_relation(relation:Blacklist):
        Manager.delete(relation=relation)


