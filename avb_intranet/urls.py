from django.urls import path
from . import views

app_name = 'avb_intranet'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('horarios/', views.horarios_view, name='horarios'),
    path('mapa/', views.mapa_view, name='mapa'),
]