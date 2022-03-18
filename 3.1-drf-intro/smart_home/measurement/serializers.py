from rest_framework import serializers
from measurement.models import Measurement, Sensor
# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    # TODO: запрос №2, 5 получение инфы по конкретному датчику. Выдается полная инфа по датчику
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorDetailUpdateSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class SensorCreateListSerializer(serializers.ModelSerializer):
    # TODO: запрос №1,  4. ID, название и описание
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class AddTemperatureSerializer(serializers.ModelSerializer):
    # TODO: запрос №3 указываются ID датчика и температура
    class Meta:
        model = Measurement
        fields = ['temperature']


class AddMeasurementSerializer(serializers.ModelSerializer):
    temperature = AddTemperatureSerializer()

    class Meta:
        model = Sensor
        fields = ['id', 'temperature']
