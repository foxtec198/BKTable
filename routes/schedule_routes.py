from flask import Blueprint, request, jsonify
from services.schedule_service import ScheduleService
from models.schedule_model import Schedule, db
from datetime import datetime

schedule_bp = Blueprint("schedule_bp", __name__)

@schedule_bp.route("/generate", methods=["GET"])
def get_schedule():
    month = int(request.args.get("month", 1))
    year = int(request.args.get("year", datetime.now().year))

    schedule = ScheduleService.get_or_create_schedule(month, year)
    return jsonify(schedule)

@schedule_bp.route("/regenerate", methods=["POST"])
def regenerate_schedule():
    data = request.get_json()
    month = data.get("month")
    year = data.get("year")

    Schedule.query.filter_by(month=month, year=year).delete()
    db.session.commit()

    schedule = ScheduleService.get_or_create_schedule(month, year)
    return jsonify(schedule)

