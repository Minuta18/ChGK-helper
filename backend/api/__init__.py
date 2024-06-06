from api import views
import shared_library

db = shared_library.DB_connection('sqlite://./app.db')
orm_base = db.get_base()

