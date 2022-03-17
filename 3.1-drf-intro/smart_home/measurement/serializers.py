from rest_framework import serializers
from measurement.models import Measurement, Sensor
# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    # TODO: запрос №5 получение инфы по конкретному датчику. Выдается полная инфа по датчику
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class SensorListSerializer(serializers.ModelSerializer):
    # TODO: запрос №4 получение списка датчиков. Выдается список с краткой инфой: ID, название и описание
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorCreateUpdateSerializer(serializers.ModelSerializer):
    # TODO: запрос №1,2 указываются название и описание датчика
    class Meta:
        model = Sensor
        fields = ['name', 'description']


class AddTemperatureSerializer(serializers.ModelSerializer):
    # TODO: запрос №3 указываются ID датчика и температура
    class Meta:
        model = Measurement
        fields = ['temperature']


class AddMeasurementSerializer(serializers.ModelSerializer):
    measurement = AddTemperatureSerializer()

    class Meta:
        model = Sensor
        fields = ['id', 'measurement']
