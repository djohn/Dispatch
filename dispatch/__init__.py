from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import NewRequest
from dispatch.datahall import DataHall
from pymongo import Connection
from gridfs import GridFS

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application."""

    session_factory = UnencryptedCookieSessionFactoryConfig('chuckNorris')

    config = Configurator(settings=settings, session_factory=session_factory)
    config.scan('dispatch')
    config.registry.mongo_conn = Connection(settings['db_address'],
                                            int(settings['db_port']))
    config.add_renderer('mongo_json', 'dispatch.renderers.MongoJSONRenderer') 
    config.add_static_view('static', 'dispatch:static')
    config.add_route('home', '/',
                     view='dispatch.views.home',
                     renderer="home.mak")
    config.add_route('request', '/request/{action}',
                     view='dispatch.requests.request',
                     renderer='mongo_json')
    config.add_route('view_all', '/view_all',
				     view='dispatch.views.view_all',
				     renderer='mongo_json')
	# Request Frontend Routes
    config.add_route('add_shout', '/add_shout',
                     view='dispatch.views.add_shout',
                     renderer="addshout.mak")
    
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
    event.request.db = db # Development Purposes Only, Remove.
    event.request.d = DataHall(db)