# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from django.core.files.base import ContentFile
import base64
from .models import Bien
from .forms import BienForm

def registrar_bien(request):
    if request.method == 'POST':
        form = BienForm(request.POST, request.FILES)
        if form.is_valid():
            bien = form.save(commit=False)

            # Procesar foto inmueble en base64
            foto_inmueble_b64 = request.POST.get('foto_inmueble')
            if foto_inmueble_b64:
                format, imgstr = foto_inmueble_b64.split(';base64,')
                ext = format.split('/')[-1]
                bien.foto_inmueble = ContentFile(base64.b64decode(imgstr), name=f"{bien.numero_inventario}_inmueble.{ext}")

            # Procesar foto etiqueta en base64
            foto_etiqueta_b64 = request.POST.get('foto_etiqueta')
            if foto_etiqueta_b64:
                format, imgstr = foto_etiqueta_b64.split(';base64,')
                ext = format.split('/')[-1]
                bien.foto_etiqueta = ContentFile(base64.b64decode(imgstr), name=f"{bien.numero_inventario}_etiqueta.{ext}")

            bien.save()
            return redirect('buscar_bien')  # redirige a la búsqueda o lista
    else:
        form = BienForm()
    return render(request, 'registrar_bien.html', {'form': form})

def buscar_bien(request):
    query = request.GET.get('numero_inventario')
    bien = None
    if query:
        try:
            bien = Bien.objects.get(numero_inventario=query)
        except Bien.DoesNotExist:
            bien = None
    return render(request, 'buscar_bien.html', {'bien': bien})