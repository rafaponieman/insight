from rest_framework import viewsets

from seekers.models import Seeker
from seekers.serializers import SeekerSerializer


class SeekerViewSet(viewsets.ModelViewSet):
    queryset = Seeker.objects.all()
    serializer_class = SeekerSerializer
