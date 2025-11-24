from datetime import date
import calendar
from models.schedule_model import db, Schedule
from services.schedular_services import SchedularService
from models.employees import Employee
from models.task import Task

class ScheduleService:
    @staticmethod
    def get_or_create_schedule(month: int, year: int):
        existing = Schedule.query.filter_by(month=month, year=year).first()
        if existing:
            return existing.data

        # Employees e Tasks poderiam vir do banco também
        employees = [
            Employee("Estefani", "segunda"),
            Employee("Luan", "terça"),
            Employee("Guilherme", "quarta"),
            Employee("Diogo", "quinta")
        ]

        tasks = [
            Task("Wash"),
            Task("Maquina"),
            Task("Cozinha", 1, 5)
        ]

        scheduler = SchedularService(employees, tasks)
        start_date = date(year, month, 1)
        days_in_month = calendar.monthrange(year, month)[1]
        schedule = scheduler.generate_schedule(start_date, days_in_month)

        # Salva no BD
        new_schedule = Schedule()
        new_schedule.month = month
        new_schedule.year = year
        new_schedule.data = schedule
        db.session.add(new_schedule)
        db.session.commit()

        return schedule
