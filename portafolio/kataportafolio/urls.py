from django.urls import path

from kataportafolio import views

app_name = 'kataportafolio'

urlpatterns = [
    path('', views.get_portafolios, name='get_portafolios'),
    path('addUser/', views.add_user_view, name='addUser'),
]
