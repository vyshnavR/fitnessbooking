from django.urls import path
from .views import FitnessClassList, BookFitnessClass, ClientBookings

urlpatterns = [
    path('classes', FitnessClassList.as_view()),
    path('book', BookFitnessClass.as_view()),
    path('bookings', ClientBookings.as_view()),
]
