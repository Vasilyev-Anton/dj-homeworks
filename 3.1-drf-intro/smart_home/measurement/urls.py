from django.urls import path

from measurement.views import SensorCreateListView, SensorDetailUpdateView, AddMeasurementView

urlpatterns = [
    path('measurement/sensors/', SensorCreateListView.as_view()),
    path('sensor/<pk>/', SensorDetailUpdateView.as_view()),
    path('measurements/<pk>/', AddMeasurementView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
