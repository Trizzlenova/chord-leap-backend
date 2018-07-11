from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from logic.models import *
from rest_framework import views, serializers, status
from rest_framework.response import Response


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()

class EchoView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED)


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        label='Username',
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        label= "Password",
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    full_name = serializers.CharField(max_length=40)
    image = serializers.CharField(max_length=250)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'full_name', 'image')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.validated_data['username']
        user.validated_data['password']
        user.save()
        return user


class ChordSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=10)
    # audio_sample = serializers.CharField(max_length=250)
    related_chords = serializers.CharField(max_length=250)
    class Meta:
        model = Chord
        fields = ('id', 'name',
         # 'audio_sample',
         'related_chords')



class ProgressionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=250)
    chords = serializers.CharField(max_length=250)

    class Meta:
        model = Progression
        fields = ('id', 'user','chords')







#class Chord_ProgressionSerializer(serializers.HyperlinkedModelSerializer):
#     bands = serializers.HyperlinkedRelatedField(
#         view_name='chords',
#         many = True
#     )
#     class Meta:
#         model = Band
#         fields = ('id', 'chords', 'length')
