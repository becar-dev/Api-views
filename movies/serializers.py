from rest_framework import serializers
from .models import Movie, Actor

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    actor = ActorSerializer(many=True)  # Many actors can be related to one movie

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        actors_data = validated_data.pop('actor')  # Separate actor data
        movie = Movie.objects.create(**validated_data)  # Create the movie instance
        for actor_data in actors_data:
            actor = Actor.objects.create(**actor_data)  # Create each actor
            movie.actor.add(actor)  # Associate the actor with the movie
        return movie