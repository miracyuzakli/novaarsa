"""Django's command-line utility for administrative tasks."""
import os
import sys
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import call_command
from django.conf import settings
from django.apps import apps

def run_periodic_task():
    # Ekrana süre bitti yazan komutunu çağır
    call_command('tarayici')


def run_scheduler():
    # Zamanlayıcıyı oluştur
    scheduler = BackgroundScheduler()

    # Her 60 saniyede bir run_periodic_task fonksiyonunu çağır
    scheduler.add_job(run_periodic_task, 'interval', seconds=60)

    # Zamanlayıcıyı başlat
    scheduler.start()