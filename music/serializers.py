from rest_framework import serializers

from music.models import Musica


class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = ('nome_da_musica', 'artista', 'genero_musical', 'link_musica')

