from rest_framework import serializers
from .models import Card, History, ExerciseCount, Contact,Streaks

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"

class ExerciseCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseCount
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class StreaksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Streaks 
        fields = "__all__"