from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.CharField('Описание', max_length=250)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.IntegerField('Температура')
    created_at = models.DateTimeField('Дата измерения', auto_now=True)
