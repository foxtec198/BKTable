from flask import Blueprint, request, jsonify
from datetime import datetime
from models.employees import Employee
from models.task import Task
from models.days import days
from services.schedular_services import SchedularService

schedule_bp = Blueprint("schedule_bp", __name__)

@schedule_bp.route("/generate", methods=['GET'])
def generate_schedule():
    dias = int(request.args.get("dias", 7))
    inicio = request.args.get("inicio", datetime.today().strftime("%Y-%m-%d"))
    start_date = datetime.strptime(inicio, "%Y-%m-%d").date()
    
    employees = [
        Employee("Estefani", days["segunda"]),
        Employee("Luan", days["terça"]),
        Employee("Guilherme", days["quarta"]),
        Employee("Diogo", days["quinta"])
    ]
    
    tasks = [
        Task("Wash"),
        Task("Maquina"),
        Task("Cozinha", 1, 5)
    ]
    
    scheduler = SchedularService(employees, tasks)
    schedule = scheduler.generate_schedule(start_date, dias)

    return jsonify(schedule)
