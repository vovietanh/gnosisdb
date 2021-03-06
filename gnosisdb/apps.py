# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.conf import settings
from celery import Celery


app = Celery('ether-logs')


class GnosisdbConfig(AppConfig):
    name = 'gnosisdb'

    def ready(self):
        app.config_from_object('django.conf:settings')
        app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, force=True)

