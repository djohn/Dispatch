from pyramid.response import Response
from dispatch.models import *
from pymongo.objectid import ObjectId
from pymongo.errors import InvalidId

# 'nc' is the preferred shorthand for the 'Node' collection in the database.

def home(request):
    
    return {}

# Request Frontend Views
def add_shout(request):

    return {}

# Development Views
def view_all(request):
    documents = request.db.node.find({}, {'_id' : 1})
    
    return 

def init(request):
    m = Node(name="Mike")
    d = Node(name="Doug")
    request.db.node.save(m.__dict__)
    request.db.node.save(d.__dict__)   
    return Response("OK")

def drop(request):
    return Response(str(request.db.node.drop()))