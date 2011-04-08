from pyramid.response import Response
from dispatch.models import *
from pymongo.objectid import ObjectId
from pymongo.errors import InvalidId
import json

def request_handler(request):
    
    # 'nc' is the preferred shorthand for the 'Node' collection in the database.
    nc = request.db.node
    try:
        nid = ObjectId(str(request.GET['id']))
    except InvalidId:
        nid = None
    
    if (nid != None):
        node = Node(db=request.db, id=nid)
               
        return json.dumps(node.__dict__, cls=JSONIdEncoder)
    else:
        return {'nodes':[{'name':'No Node Found.', '_id':'Try entering a different Id, check that the Id is valid, or check the database.'}]}
    
    return  {"_id": "4d99907f7d777d65c0000004", "name": "Test"}

class JSONIdEncoder(json.JSONEncoder):
    def default(self, o):
        if (type(o) is ObjectId):
            return str(o)
        else:
            return json.JSONEncoder.default(self, o)