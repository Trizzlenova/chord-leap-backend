from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.forms import ModelForm
from logic.models import User, Chord, Progression

# Create your views here.

class Chord:
    def __init__(self, name, related_chord):
        self.name = name
        self.related_chord = related_chord

chords = [
    Chord('Emin', ['D maj, A min', 'G maj']),
    Chord('Amin', ['C maj, E min', 'B maj']),
    Chord('Bmin', ['F maj, G min', 'A maj']),
]

def index(request):
    return render(request, 'index.html', {'chords': chords})

def chord_list(request):
    chords = Chord.objects.all()
    return render(request, 'index.html', {'chords': chords})

