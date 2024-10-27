from rest_framework import serializers
from moves.models import movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=movie
        fields= "__all__"