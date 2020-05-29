from flask import Flask, session, jsonify
from db.db import initialize_db
from views.users import users
from views.hotels import hotels
from views.reservations import reservations

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/smart_shop'
}

initialize_db(app)

app.register_blueprint(users)
app.register_blueprint(hotels)
app.register_blueprint(reservations)

if __name__ == "__main__":
    app.run()
