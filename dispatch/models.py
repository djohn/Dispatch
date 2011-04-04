class Node:
    def __init__(self, **kwargs):
        self.name = None
        self.parent = None
        self.content = None
        self.id = None
        for key in kwargs:
            if (key == "name"):
                self.name = kwargs[key]
            if (key == "node"):
                node = kwargs[key]
                self.id = node['_id']
                for field in node:
                    if (field == 'parent'):
                        self.parent = node['parent']
                    if (field == 'content'):
                        self.content = node['content']
            else:
                if (key == "_id"):
                    self.id = kwargs[key]
                if (key == "parent"):
                    self.parent = kwargs[key]
                if (key == "content"):
                    self.content = kwargs[key]
    
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