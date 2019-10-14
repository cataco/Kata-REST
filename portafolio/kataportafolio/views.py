import json

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth import authenticate

from kataportafolio.models import Portafolio


@csrf_exempt
def get_portafolios(request):
    portafolios_list = Portafolio.objects.all()
    if request.GET.get('id_persona'):
        portafolios_list = portafolios_list.filter(publico=True).filter(user__id=request.GET.get('id_persona'))
    return HttpResponse(serializers.serialize("json", portafolios_list))


@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        if 'id' in json_user:
            first_name = json_user['first_name']
            last_name = json_user['last_name']
            password = json_user['password']

            user_model = User.objects.get(id=json_user['id'])
            user_model.first_name = first_name
            user_model.last_name = last_name
            user_model.password = password
        else:
            json_user = json.loads(request.body)
            username = json_user['username']
            first_name = json_user['first_name']
            last_name = json_user['last_name']
            password = json_user['password']
            email = json_user['email']

            user_model = User.objects.create_user(username=username, password=password)
            user_model.first_name = first_name
            user_model.last_name = last_name
            user_model.email = email
    user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))

def user_login(request):
        user_params = json.loads(request.body)
        user = authenticate(username=user_params['username'], password=user_params['password'])
        if user is not None:
            return JsonResponse({'status': 'Authenticated'})
        else:
            return JsonResponse({'status': 'Error'})
