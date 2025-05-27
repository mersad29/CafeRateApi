# Serializers
from rest_framework import serializers

from Cafe.models import Review, Cafe


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'rating', 'comment', 'created_at']


class CafeSerializer(serializers.ModelSerializer):
    average_rating = serializers.ReadOnlyField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Cafe
        fields = ['id', 'name', 'location', 'phone', 'website', 'hours',
                  'description', 'image', 'average_rating', 'reviews',
                  'created_at', 'updated_at']


class CafeListSerializer(serializers.ModelSerializer):
    average_rating = serializers.ReadOnlyField()

    class Meta:
        model = Cafe
        fields = ['id', 'name', 'location', 'average_rating', 'image']