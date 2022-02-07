from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine


DB = PostgresEngine(config={
    "database":"leep2db",
    "user":"lg",
    "password":"l123",
    "host":"localhost",
    "port":"5432",
})



APP_REGISTRY = AppRegistry(apps=['legal.piccolo_app','piccolo_admin.piccolo_app'])
