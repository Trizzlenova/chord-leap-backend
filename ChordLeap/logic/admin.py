from django.contrib import admin
from .models import User, Chord , Progression

# Register your models here.
admin.site.register(User)
admin.site.register(Chord)
admin.site.register(Progression)
