from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), # Ao acessar a raiz('/') chamara a view index
    path('historia1', views.historia1, name='historia1'), # Ao acessar '/historia1' chamara a view historia1
    path('historia2', views.historia2, name='historia2'), # Ao acessar '/historia2' chamara a view historia2
    path('ajaxhistoria1', views.ajaxhistoria1, name='ajaxhistoria1'), # O ajax usará para chamar a view ajaxhistoria1
    path('ajaxiniciarjogo', views.ajaxiniciarjogo, name='ajaxiniciarjogo'), # O ajax usara para chama a view ajaxiniciarjogo
    path('ajaxstatus', views.ajaxstatus, name='ajaxstatus'), # O ajax usara para chama a view ajaxstatus


    path('ajaxhistoria2', views.ajaxhistoria2, name='ajaxhistoria2'), # O ajax usará para chamar a view ajaxhistoria2
    path('desenvolvimento', views.desenvolvimento, name='desenvolvimento'), # URL para DEBUG, chamara a view desenvolvimento
    path('ajaxdesenvolvimento', views.ajaxdesenvolvimento, name='ajaxdesenvolvimento'), # Ajax para DEBUG, chamara a view ajaxdesenvolvimento
    
]