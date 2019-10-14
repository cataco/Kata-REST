from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers



@csrf_exempt
def get_portafolios(request):
    portafolios_list =  []
    return HttpResponse(serializers.Serializer("json", portafolios_list))
