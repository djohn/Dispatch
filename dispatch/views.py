from pyramid.response import Response
from dispatch.models import *
from pymongo.objectid import ObjectId
from pymongo.errors import InvalidId

# 'nc' is the preferred shorthand for the 'Node' collection in the database.

def home(request):
    nc = request.db.node
    nodes = []
    for n in nc.find():
        nodes.append(n)
    
    return {'nodes': nodes}

def view_node(request):
    nc = request.db.node
    try:
        nid = ObjectId(str(request.matchdict['node']))
    except InvalidId:
        nid = None
    else:
        node = Node(db=request.db, id=nid)
    
    if (nid != None):
        n = Node(node=dbnode)
        ndict = {}
        
        ndict
        
        
        return {}
    else:
        return {'nodes':[{'name':'No Node Found.', '_id':'Try entering a different Id, check that the Id is valid, or check the database.'}]}


# <!-- Development Views

def init(request):
    newShout = Shout()
    nsId1 = newShout.save(request.db)
    nsId2 = newShout.save(request.db)
    nsId3 = newShout.save(request.db)
    subNode = Node(name='Thread', content=[{'type':'shout', '_id':nsId1, 'flag':'active'},
                                           {'type':'shout', '_id':nsId2, 'flag':'active'}])
    subnodeId = subNode.save(request.db)
    newNode = Node(name='Test', content=[{'type':'node', '_id':subnodeId, 'flag':'active'},
                                         {'type':'shout', '_id':nsId3, 'flag':'active'}])
    newNode.save(request.db)
    return Response("OK")

def drop(request):
    return Response(str(request.db.node.drop()))

# --!>