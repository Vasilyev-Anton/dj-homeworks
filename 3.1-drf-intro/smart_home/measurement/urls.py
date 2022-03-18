from django.urls import path

from measurement.views import SensorCreateListView, SensorDetailUpdateView, AddMeasurementView

urlpatterns = [
    path('sensors/', SensorCreateListView.as_view()),
    path('sensors/<pk>/', SensorDetailUpdateView.as_view()),
    path('measurements/', AddMeasurementView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
