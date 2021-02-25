import os

# Web service host and port configuration
host = "127.0.0.1"
port = "5000"

# SQL light DB path configuration
db_path = os.path.join(os.path.dirname(__file__), 'urlapp.db')
db_uri = 'sqlite:///{}'.format(db_path)
