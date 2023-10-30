from rest_framework import viewsets

from seekers.models import Run, Seeker, Training
from seekers.serializers import RunSerializer, SeekerSerializer, TrainingSerializer


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer


class SeekerViewSet(viewsets.ModelViewSet):
    queryset = Seeker.objects.all()
    serializer_class = SeekerSerializer


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
