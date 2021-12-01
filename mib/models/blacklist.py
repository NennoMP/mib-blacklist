from mib import db


class Blacklist(db.Model):
   
    '''Auxiliary table for mantaining records of blocked users for each user.'''
    __tablename__ = 'Blacklist'

    # Data
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer)
    id_blocked = db.Column(db.Integer)

    def __init__(self, *args, **kw):
        super(Blacklist, self).__init__(*args, **kw)

    
    def set_relationship(self, blocking_user:int, blocked_user:int):
        self.id_user = blocking_user
        self.id_blocked = blocked_user
