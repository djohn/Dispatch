from pyramid.response import Response
from dispatch.models import *
from pymongo.objectid import ObjectId

def request_handler(request):
    
    
    
    return  request.GET.items()