from rest_framework import viewsets
from .serializer import CitaSerializer
from .models import Cita

# Create your views here.


class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
