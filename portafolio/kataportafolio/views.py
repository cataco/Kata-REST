from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers

from kataportafolio.models import Portafolios


@csrf_exempt
def get_portafolios(request):
    images_list = Portafolios.objects.all()
    return HttpResponse(serializers.Serializer("json", images_list))
