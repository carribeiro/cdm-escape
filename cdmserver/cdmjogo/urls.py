from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), # Ao acessar a raiz('/') chamara a view index
    path('historia1', views.historia1, name='historia1'), # Ao acessar '/historia1' chamara a view historia1
    path('historia2', views.historia2, name='historia2'), # Ao acessar '/historia2' chamara a view historia2
    path('ajaxhistoria1', views.ajaxhistoria1, name='ajaxhistoria1'), # O ajax usará para chamar a view ajaxhistoria1
    path('ajaxiniciarjogo', views.ajaxiniciarjogo, name='ajaxiniciarjogo'), # O ajax usara para chama a view ajaxiniciarjogo
    path('ajaxstatus', views.ajaxstatus, name='ajaxstatus'), # O ajax usara para chama a view ajaxstatus

    # não chegou a ser usada
    #path('ajaxhistoria2', views.ajaxhistoria2, name='ajaxhistoria2'), # O ajax usará para chamar a view ajaxhistoria2

    path('desenvolvimento', views.desenvolvimento, name='desenvolvimento'), # URL para DEBUG, chamara a view desenvolvimento
    path('ajaxdesenvolvimento', views.ajaxdesenvolvimento, name='ajaxdesenvolvimento'), # Ajax para DEBUG, chamara a view ajaxdesenvolvimento
    path('teste_cartoes', views.teste_cartoes, name='teste_cartoes'), # URL de teste dos sinais dos cartões (loop de teste dos três)
    path('teste_banheiro', views.teste_banheiro, name='teste_banheiro'), # URL de teste dos sinais do banheiro
    path('teste_diversos', views.teste_diversos, name='teste_diversos'), # URL de teste dos sinais do caminho da energia, lavanderia, gaveta e interno da geladeira

    path('ajaxdebugstatus', views.ajaxdebugstatus, name='ajaxdebugstatus'), # O ajax usara para chama a view ajaxdebugstatus

    # URLs exclusivas para DEBUG; TODO: criar uma única thread de DEBUG associada a chamadas AJAX para executar em background
    path('resetleds', views.resetleds, name='resetleds'), 
    path('setleds', views.setleds, name='setleds'), 
    path('setledhi', views.setledhi, name='setledhi'), 
    path('setledlo', views.setledlo, name='setledlo'), 
    path('setspotcode', views.setspotcode, name='setspotcode'), 
    path('setbateria', views.setbateria, name='setbateria'), 
    path('setgeladeira', views.setgeladeira, name='setgeladeira'), 

    path('resetcartaogeladeira', views.resetcartaogeladeira, name='resetcartaogeladeira'), 
    path('resetcartaomicroondas', views.resetcartaomicroondas, name='resetcartaomicroondas'), 
    path('resetcartaolavadora', views.resetcartaolavadora, name='resetcartaolavadora'), 

    path('pulso_abrir_banheiro', views.pulso_abrir_banheiro, name='pulso_abrir_banheiro'), 
    path('pulso_abrir_geladeira', views.pulso_abrir_geladeira, name='pulso_abrir_geladeira'), 
    path('pulso_abrir_gaveta_banheiro', views.pulso_abrir_gaveta_banheiro, name='pulso_abrir_gaveta_banheiro'), 
    path('pulso_abrir_gaveta_armario', views.pulso_abrir_gaveta_armario, name='pulso_abrir_gaveta_armario'), 
    path('pulso_abrir_porta_armario', views.pulso_abrir_porta_armario, name='pulso_abrir_porta_armario'), 
    path('pulso_abrir_gaveta_aparador', views.pulso_abrir_gaveta_aparador, name='pulso_abrir_gaveta_aparador'), 
    path('pulso_abrir_bau', views.pulso_abrir_bau, name='pulso_abrir_bau'), 
]