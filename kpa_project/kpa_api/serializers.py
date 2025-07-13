from rest_framework import serializers
from .models import WheelSpecification

class WheelSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields = '__all__'
        extra_kwargs = {
            'form_number': {'required': True},
            'submitted_by': {'required': True},
            'submitted_date': {'required': True},
            'fields': {'required': True},
        }
