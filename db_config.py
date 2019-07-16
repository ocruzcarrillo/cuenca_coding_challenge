import sqlalchemy as db

# Data Base params to connect
try:
    from config.default_config import *
except ImportError:
    pass

# If exists an local config file, we load the DB params
try:
    from config.local_config import *
except ImportError:
    pass

table_name = 'solutions'
engine = db.create_engine('postgresql+psycopg2://{}:{}@localhost:5432/{}'.format(db_user, db_password, db_name))
connection = engine.connect()
metadata = db.MetaData()
metadata.bind = engine

solutions_table = db.Table(table_name, metadata,
          db.Column('id', db.Integer, primary_key=True, nullable=False),
          db.Column('board_size', db.Integer),
          db.Column('solution', db.String))

# Create the solutions Table if don't exists
if not engine.dialect.has_table(connection, table_name):
    metadata.create_all()
