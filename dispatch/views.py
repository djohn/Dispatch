from pyramid.response import Response
from dispatch.models import *
from pymongo.objectid import ObjectId
from pymongo.errors import InvalidId

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
        dbnode = None
    else:
        dbnode = nc.find_one({"_id":nid})
        
    if (dbnode != None):
        n = Node(node=dbnode)
        return {'nodes':[{'name':str(n.name), '_id':str(n.id)}]}
    else:
        return {'nodes':[{'name':'No Node Found.', '_id':'Try entering a different Id, check that the Id is valid, or check the database.'}]}


# <!-- Development Views

def init(request):
    newShout = Shout()
    nsId1 = newShout.save(request.db)
    nsId2 = newShout.save(request.db)
    nsId3 = newShout.save(request.db)
    subNode = Node(name='Thread', content=[{'type':'shout', 'id':nsId1, 'flag':'active'},
                                           {'type':'shout', 'id':nsId2, 'flag':'active'}])
    subnodeId = subNode.save(request.db)
    newNode = Node(name='Test', content=[{'type':'node', 'id':subnodeId, 'flag':'active'},
                                         {'type':'shout', 'id':nsId3, 'flag':'active'}])
    newNode.save(request.db)
    return Response("OK")

def drop(request):
    return Response(str(request.db.node.drop()))

# --!>