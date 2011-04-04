from pyramid.response import Response
from dispatch.models import *

def home(request):
    node = Node('Test', node=request.db.node.find_one({"name":"Test"}))
    return {'node':node.name, 'id':str(node.id), 'content':node.content}

def init(request):
    newNode = Node('Test', content='Some coded DB content')
    newNode.save(request.db)
    return Response("OK")