from pymongo.objectid import ObjectId
from dispatch.models import *

class DataHall():
    def __init__(self, db):
        self.db = db
        self.dispatch = Dispatcher(self)
        self.recall = Recaller(self)

class Dispatcher():
    def __init__(self, datahall):
        self.dh = datahall
        self.db = self.dh.db
        
    def add_shout(self, s):
        if isinstance(s, list):
            sids = []
            for shout in s:
                # Recursive adding for multiple shouts
                sids.append(self.addShout(shout))
            return sids
        elif isinstance(s, Shout):
            sid = self.db.shout.save(s.__dict__)
            s._id = sid
            # Dispatches shout to nodes, and node members.
            self.dispatch_shout(s.recipients, s)
            return sid
        else:
            raise TypeError('Only Model classes can be saved by the dispatcher.')
    
    def dispatch_shout(self, recipients, shout):
        for r in recipients:
            self.db.node.update({'_id': r},
                                { '$addToSet' : { 'active_content':shout._id }})
            rmems = self.db.node.find({'_id':r}, {'members':1})
            # This should be changed from recursion to gathering a list
            #              for a multiple update call before production
            self.dispatch_shout(rmems, shout)

class Recaller():
    def __init__(self, datahall):
        self.dh = datahall
        self.db = self.dh.db
        
    def node_by_id(self, id):
        document = self.db.node.find_one({'_id':id})
        return Node(document['_id'], document['name'], document['content'])
        
    def shout_by_id(self, id):
        document = self.db.shout.find_one({'_id':id})
        return Shout(document['_id'], document['name'], document['content'])
        
        
        
        