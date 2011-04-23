from pyramid.response import Response
from dispatch.models import *
from pymongo import json_util

def request(request):
    action = request.matchdict['action']
    if (action == "add_shout"):
        recipients = str.split(str(request.params['recipients']), ',')
        
        shout = Shout(owner=request.params['owner'],
                      name=request.params['name'],
                      access=request.params['access'],
                      recipients=recipients,
                      content=request.params['content'])
        
        sid = request.d.dispatch.add_shout(shout)
        return str(sid)
    else:
        return Response(request.matchdict['action'])