from pymongo.objectid import ObjectId
from pymongo.errors import InvalidId

class Node(object):
    def __init__(self, name="Unnamed", parent=None, members={}, acontent=[], dcontent=[], id=None):
        self.name = name
        self.parent = parent
        self.members = members
        self.active_content = acontent
        self.dead_content = dcontent
        if id is not None:
            if isinstance(id, str):
                try:
                    nid = ObjectId(str(request.matchdict['node']))
                except InvalidId:
                    nid = None
                else:
                    self._id = nid
            elif isinstance(id, ObjectId):
                self._id = id
            else:
                raise TypeError('Invalid Id Provided: Did you specify id before saving?')

class Shout(object):
    def __init__(self, owner=None, name=None, access="private", recipients=[], content=None, id=None):
        self.owner = owner
        self.name = name
        self.access = access
        self.recipients = []
        for r in recipients:
            if isinstance(r, str):
                try:
                    nid = ObjectId(str(r))
                except InvalidId:
                    pass
                else:
                    self.recipients.append(nid)
            elif isinstance(r, ObjectId):
                self.recipients.append(r)
        self.content = content
        if id is not None:
            if isinstance(id, str):
                try:
                    nid = ObjectId(str(request.matchdict['node']))
                except InvalidId:
                    nid = None
                else:
                    self._id = nid
            elif isinstance(id, ObjectId):
                self._id = id
            else:
                raise TypeError('Invalid Id Provided: Did you specify id before saving?')