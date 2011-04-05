class Node:
    def __init__(self, **kwargs):
        self.name = None
        self.parent = None
        self.content = None
        self.id = None
        for key in kwargs:
            if (key == "node"):
                node = kwargs[key]
                self.id = node['_id']
                for field in node:
                    if (field == 'parent'):
                        self.parent = node['parent']
                    if (field == 'content'):
                        self.content = node['content']
                    if (field == 'name'):
                        self.name = node['name']
            else:
                if (key == "_id"):
                    self.id = kwargs[key]
                if (key == "parent"):
                    self.parent = kwargs[key]
                if (key == "content"):
                    self.content = kwargs[key]
                if (key == "name"):
                    self.name = kwargs[key]
    
    def save(self, db):
        nodedoc = {}
        if (self.name != None):
            nodedoc['name'] = self.name
        if (self.parent != None):
            nodedoc['parent'] = self.parent
        if (self.content != None):
            nodedoc['content'] = self.content
        if (self.id != None):
            nodedoc['_id'] = self.id
        return db.node.save(nodedoc, safe=True)

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
        