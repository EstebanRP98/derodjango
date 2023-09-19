from django_crontab.crontab import CronTab
from datetime import datetime, timedelta
from .models import Cita


def my_daily_task():
    # Obtén la fecha actual
    today = datetime.now().date()

    # Calcula la fecha un día antes
    yesterday = today - timedelta(days=1)

    # Busca todas las citas con fecha de inicio igual a ayer
    citas_a_cancelar = Cita.objects.filter(fecha_inicio__date=yesterday)

    # Actualiza el estado de las citas encontradas a "CANCELADO"
    for cita in citas_a_cancelar:
        cita.status = "CANCELADO"
        cita.save()

    # Registra información en el registro de tareas programadas
    CronTab.log.info("Tarea diaria ejecutada con éxito.")
