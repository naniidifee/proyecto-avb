from django.shortcuts import render

def index_view(request):
    return render(request, 'avb_intranet/index.html')

def horarios_view(request):
    # HU03, HU06, HU11
    return render(request, 'avb_intranet/horarios.html')

def mapa_view(request):
    # HU07, HU09
    return render(request, 'avb_intranet/mapa.html')