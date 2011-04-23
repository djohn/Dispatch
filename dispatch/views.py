from pyramid.response import Response
from dispatch.models import *
from pymongo.objectid import ObjectId
from pymongo.errors import InvalidId

# 'nc' is the preferred shorthand for the 'Node' collection in the database.

def home(request):
    
    return {}
    
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
    m = Node(name="Mike")
    d = Node(name="Doug")
    request.db.node.save(m.__dict__)
    request.db.node.save(d.__dict__)   
    return Response("OK")

def drop(request):
    return Response(str(request.db.node.drop()))

# --!>