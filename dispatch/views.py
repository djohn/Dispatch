from pyramid.response import Response

def home(request):
    content = request.db.node.find_one({"name":"Test"})
    return {'node':'Test', 'content':content['content']}

def init(request):
    request.db.node.insert({"node":"Test", "content":"Some DB Content"})
    return Response("OK")
