from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from kataportafolio.models import Portafolio


@csrf_exempt
def get_portafolios(request):
    portafolios_list = Portafolio.objects.all()
    return HttpResponse(serializers.serialize("json", portafolios_list))
