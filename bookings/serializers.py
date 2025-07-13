from rest_framework import serializers
from .models import FitnessClass, Booking

# class FitnessClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FitnessClass
#         fields = ['id', 'name', 'datetime', 'instructor', 'available_slots']

from django.utils import timezone

class FitnessClassSerializer(serializers.ModelSerializer):
    datetime = serializers.SerializerMethodField()

    class Meta:
        model = FitnessClass
        fields = ['id', 'name', 'datetime', 'instructor', 'available_slots']

    def get_datetime(self, obj):
        local_dt = timezone.localtime(obj.datetime)
        return local_dt.strftime("%d-%m-%Y %I %p") 



class BookingSerializer(serializers.ModelSerializer):
    timestamp = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = ['id', 'fitness_class', 'client_name', 'client_email', 'timestamp']

    def get_timestamp(self, obj):
        local_ts = timezone.localtime(obj.timestamp)
        return local_ts.strftime("%d-%m-%Y %I:%M %p")
