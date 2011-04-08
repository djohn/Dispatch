from pymongo.objectid import ObjectId

class Node(object):
    def __init__(self, db=None, id=None):
        self._id = None
        self.name = None
        self.content = None
        if (db != None and type(id) is ObjectId):
                dbnode = db.node.find_one({'_id':id})
                self._id = str(dbnode['_id'])
                self.name = dbnode['name']
                self.content = dbnode['content']
                del dbnode
            

class Shout:
    def __init__(self, **kwargs):
        self.name = None
        self.content = None
        for key in kwargs:
            if (key == "shout"):
                shout = kwargs[key]
                self.id = shout['_id']
                self.name = shout['name']
                self.content = shout['content']
        if (self.name == None):
            self.name = 'Test Shout'
            self.content = 'This is a test shout.'
                
    def save(self, db):
        shoutdoc = {'name':self.name, 'content':self.content}
        return db.shout.save(shoutdoc)