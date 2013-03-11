#coding=utf-8
''' base business '''

from database import Database

class Base(object):
    ''' base business '''

    def __init__(self):
        self.db = Database.instance()
        self.session = self.db.get_session()
        self.error_dict = dict({})

    def _insert(self, mod_obj):
        self.session.add(mod_obj)
        self.session.commit()

    def _update(self, mod_obj, update_dict):
        mod_obj.update(category)
        self.session.commit()

    def _delete(self, mod_obj):
        self.session.commit()
