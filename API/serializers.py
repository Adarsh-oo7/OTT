from rest_framework import serializers
from moves.models import movie
from moves.models import watch_history,watch_list


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=movie
        fields= "__all__"


class MovieHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = watch_history
        fields = "__all__"



class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = watch_list
        fields = "__all__"