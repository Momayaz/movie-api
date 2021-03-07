from rest_framework import serializers
from .models import MoviesData


class Serilaizer_Movie(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = MoviesData
        fields = ['id', 'name', 'duration', 'about', 'rating', 'typ', 'image']