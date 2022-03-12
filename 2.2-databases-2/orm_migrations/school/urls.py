from django.urls import path, include

from school.views import students_list

urlpatterns = [
    path('', students_list, name='students'),
    path('debug/', include('debug_toolbar.urls')),
]

