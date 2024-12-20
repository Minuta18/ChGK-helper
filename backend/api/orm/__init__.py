import shared_library

db = shared_library.DB_connection(
    'postgresql+psycopg2://admin:test@server.mrvasil.ru:4001/postgres')
orm_base = db.get_base()
