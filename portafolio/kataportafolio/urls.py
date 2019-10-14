from django.urls import path

from kataportafolio import views

app_name = 'kataportafolio'

urlpatterns = [
    path('', views.get_portafolios, name='get_portafolios'),
    path('addUser/', views.add_user_view, name='addUser'),
    #path('portafolio/getInfo/<int:user_id>', views.get_view_public_info),
    path('login/', views.user_login)
]
