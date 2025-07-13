from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
from django.utils import timezone
import logging
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
logger = logging.getLogger(__name__)




class FitnessClassList(generics.ListAPIView):
    serializer_class = FitnessClassSerializer

    def get_queryset(self):
        return FitnessClass.objects.filter(datetime__gte=timezone.now()).order_by('datetime')

class BookFitnessClass(APIView):
    def post(self, request):
        class_id = request.data.get("class_id")
        name = request.data.get("client_name")
        email = request.data.get("client_email")

        # Check for missing fields
        if not (class_id and name and email):
            logger.warning("Booking attempt with missing fields.")
            return Response({"error": "All fields are required."}, status=400)

        # Email validation
        try:
            validate_email(email)
        except ValidationError:
            logger.warning(f"Invalid email format: {email}")
            return Response({"error": "Invalid email format."}, status=400)

        # Get the class
        try:
            fclass = FitnessClass.objects.get(id=class_id)
        except FitnessClass.DoesNotExist:
            logger.warning(f"Class not found for ID: {class_id}")
            return Response({"error": "Class not found."}, status=404)

        # Disallow booking past classes
        if fclass.datetime < timezone.now():
            logger.info(f"Attempted to book past class: {fclass.name}")
            return Response({"error": "Cannot book a past class."}, status=400)

        # Disallow overbooking
        if fclass.available_slots <= 0:
            logger.info(f"No slots available for class: {fclass.name}")
            return Response({"error": "No slots available."}, status=400)

        # Prevent duplicate booking
        if Booking.objects.filter(fitness_class=fclass, client_email=email).exists():
            logger.info(f"Duplicate booking attempt: {email} for class {fclass.name}")
            return Response({"error": "This email has already booked this class."}, status=400)

        # create booking
        Booking.objects.create(
            fitness_class=fclass,
            client_name=name,
            client_email=email
        )
        fclass.available_slots -= 1
        fclass.save()

        logger.info(f"Booking successful: {email} booked {fclass.name}")
        return Response({"message": "Booking successful."}, status=201)


class ClientBookings(APIView):
    def get(self, request):
        email = request.GET.get("email")
        if not email:
            return Response({"error": "Email is required."}, status=400)
        
        # Email validation
        try:
            validate_email(email)
        except ValidationError:
            logger.warning(f"Invalid email format: {email}")
            return Response({"error": "Invalid email format."}, status=400)
        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
