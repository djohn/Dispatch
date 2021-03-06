from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import NewRequest
from pymongo import Connection

import pymongo
from gridfs import GridFS

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.scan('dispatch')
    config.registry.mongo_conn = pymongo.Connection(settings['db_address'], int(settings['db_port']))
    config.add_static_view('static', 'dispatch:static')
    config.add_route('home', '/', view='dispatch.views.home', renderer="home.mak")
    config.add_route('view_node', '/node/{node}', view='dispatch.views.view_node', renderer="node.mak")
    
    # Development Routes
    config.add_route('initdb', '/init', view='dispatch.views.init')
    config.add_route('dropdb', '/drop', view='dispatch.views.drop')
    # --
    
    return config.make_wsgi_app()

@subscriber(NewRequest)
def add_mongo_db(event):
    reg = event.request.registry
    settings = reg.settings
    db_name = settings['db_name']
    db = reg.mongo_conn[db_name]
    event.request.db = db