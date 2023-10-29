from rest_framework import serializers

from seekers.models import Seeker


class SeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seeker
        exclude = []
