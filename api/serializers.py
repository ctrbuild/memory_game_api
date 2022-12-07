from rest_framework import serializers
from memorygame.models import Card, Score

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Card
        fields='__all__'


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Score
        fields='__all__'