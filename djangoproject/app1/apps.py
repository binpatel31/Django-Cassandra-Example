from django.apps import AppConfig
from django.conf import settings

from cassandra.cqlengine import connection
from cassandra.cluster import Cluster


class App1Config(AppConfig):
    name = 'app1'
    def ready(self):
        session = Cluster(['127.0.0.1']).connect()
#       session.row_factory = dict_factory
        connection.register_connection(str(session), session=session)
        connection.set_default_connection(str(session))
        settings.CONNECTION = [connection,session]
