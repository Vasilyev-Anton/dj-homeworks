from django.urls import path

from measurement.views import SensorListView, SensorDetailView

urlpatterns = [
    path('measurement/sensors/', SensorListView.as_view()),
    path('sensor/<pk>/', SensorDetailView.as_view())
    # TODO: зарегистрируйте необходимые маршруты
]
