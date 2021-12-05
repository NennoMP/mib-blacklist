from mib import db


class Manager(object):
    db_session = db.session

    @staticmethod
    def check_none(**kwargs):
        """Check if given parameters are none, before setting them."""

        for name, arg in zip(kwargs.keys(), kwargs.values()):
            if arg is None:
                raise ValueError('You can\'t set %s argument to None' % name)

    @staticmethod
    def create(**kwargs):
        """Create a new relationship, in the database."""

        Manager.check_none(**kwargs)
        for bean in kwargs.values():
            db.session.add(bean)
        db.session.commit()
    
    @staticmethod
    def delete(**kwargs):
        """Delete a relationship, in the database."""

        Manager.check_none(**kwargs)
        for bean in kwargs.values():
            db.session.delete(bean)
        db.session.commit()
