# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailUpdateSerializer, SensorCreateListSerializer, AddTemperatureSerializer


class SensorCreateListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorCreateListSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SensorDetailUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailUpdateSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class AddMeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = AddTemperatureSerializer




