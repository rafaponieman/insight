from rest_framework import serializers

from seekers.models import Run, Seeker, Training


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        exclude = []


class SeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seeker
        exclude = []


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        exclude = []
