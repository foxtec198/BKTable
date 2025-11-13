from flask import Flask, jsonify
from routes.schedule_routes import schedule_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(schedule_bp, url_prefix="/api/schedule")
    return app

if __name__ == '__main__':
    create_app().run(debug=True, host="0.0.0.0", port=5005)