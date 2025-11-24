from flask import Flask
from models.schedule_model import db
from routes.schedule_routes import schedule_bp
from os import getenv

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(schedule_bp, url_prefix='/api/schedule')

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(
        debug=True, 
        host="0.0.0.0", 
        port=int(getenv("PORT", 5005))
    )