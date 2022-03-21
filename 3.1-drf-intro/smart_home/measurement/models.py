from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.CharField('Описание', max_length=250)

    # def __str__(self):
    #     return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField('Температура')
    created_at = models.DateTimeField('Дата измерения', auto_now_add=True)
    updated_at = models.DateTimeField('Дата измерения', auto_now=True)
