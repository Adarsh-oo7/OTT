from rest_framework import serializers
from moves.models import movie, watch_history, watch_list


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = ['id', 'title', 'description', 'thumbnail', 'video', 'count']  # Only include necessary fields



class MovieHistorySerializer(serializers.ModelSerializer):
    movie_details = MovieSerializer(source='movie', read_only=True)  # Nested serializer for movie details

    class Meta:
        model = watch_history
        fields = ['id', 'user', 'movie_details', 'date_time']  #

class WatchListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField() 
    movie = MovieSerializer(source='movie_id')  

    class Meta:
        model = watch_list
        fields = ["user", "movie"]  