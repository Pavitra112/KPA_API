from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer

@api_view(['GET', 'POST'])
def wheel_spec_api(request):
    if request.method == 'POST':
        serializer = WheelSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Wheel specification submitted successfully.",
                "data": {
                    "formNumber": serializer.data["form_number"],
                    "submittedBy": serializer.data["submitted_by"],
                    "submittedDate": serializer.data["submitted_date"],
                    "status": serializer.data["status"]
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        filters = {}
        if request.GET.get('formNumber'):
            filters['form_number'] = request.GET['formNumber']
        if request.GET.get('submittedBy'):
            filters['submitted_by'] = request.GET['submittedBy']
        if request.GET.get('submittedDate'):
            filters['submitted_date'] = request.GET['submittedDate']

        queryset = WheelSpecification.objects.filter(**filters)
        serializer = WheelSpecificationSerializer(queryset, many=True)
        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
