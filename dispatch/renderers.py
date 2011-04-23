import json 
from pymongo import json_util

class MongoJSONRenderer: 
        def __init__(self, info): 
                """ Constructor: info will be an object having the the 
                following attributes: name (the renderer name), package 
                (the package that was 'current' at the time the 
                renderer was registered), type (the renderer type 
                name), registry (the current application registry) and 
                settings (the deployment settings dictionary).  """ 
        def __call__(self, value, system): 
                """ Call a the renderer implementation with the value 
                and the system value passed in as arguments and return 
                the result (a string or unicode object).  The value is 
                the return value of a view.      The system value is a 
                dictionary containing available system values 
                (e.g. view, context, and request). """ 
                request = system.get('request') 
                if request is not None: 
                        if not hasattr(request, 'response_content_type'): 
                                request.response_content_type = 'application/json' 
                return json.dumps(value, default=json_util.default)