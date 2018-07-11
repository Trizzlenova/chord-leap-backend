from logic.models import *
from logic.serializers import *
from rest_framework import generics


class ChordList(generics.ListCreateAPIView):
    queryset = Chord.objects.all()
    serializer_class = ChordSerializer
