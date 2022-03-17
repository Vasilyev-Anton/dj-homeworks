# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, get_object_or_404
from measurement.models import Sensor
from measurement.serializers import SensorListSerializer, SensorDetailSerializer, SensorCreateUpdateSerializer, \
    AddMeasurementSerializer


class SensorListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class CreateSensorView(CreateAPIView):
    serializer_class = SensorCreateUpdateSerializer

    def perform_create(self, serializer):
        sensor = get_object_or_404(Sensor, name=self.request.data.get('name'), description=self.request.data.get('description'))
        return serializer.save(sensor=sensor)


class UpdateSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorCreateUpdateSerializer


class AddMeasurementView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = AddMeasurementSerializer
