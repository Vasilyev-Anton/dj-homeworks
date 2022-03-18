# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny

from measurement.models import Sensor
from measurement.serializers import AddMeasurementSerializer, SensorDetailUpdateSerializer, SensorCreateListSerializer


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


class AddMeasurementView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = AddMeasurementSerializer

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
