from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import PhoneNumberLocation
from .serializers import PhoneNumberLocationSerializer
import phonenumbers
from phonenumbers import parse, is_valid_number

class PhoneNumberLocationViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumberLocation.objects.all()
    serializer_class = PhoneNumberLocationSerializer

def validate_phone_number(phone_number):
    try:
        parsed_number = parse(phone_number, None)
        return is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberFormatException:
        return False

def my_api_view(request):
    phone_number = request.data.get('phone_number')

    if validate_phone_number(phone_number):
        # Phone number is valid, continue with your API logic
        # For example, you can create a PhoneNumberLocation object here
        # ...
        return Response({"message": "Phone number is valid"}, status=status.HTTP_200_OK)
    else:
        # Phone number is not valid, return an error response
        return Response({"error": "Invalid phone number"}, status=status.HTTP_400_BAD_REQUEST)
