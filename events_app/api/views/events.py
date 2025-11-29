from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from events_app.models.events import EventModel
from events_app.api.serializers.events import EventSerializer


class EventViewSet(ModelViewSet):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data.get('joined_users') is None:
            serializer.validated_data['joined_users'] = [request.user]
        else:
            serializer.validated_data['joined_users'].append(request.user)

        serializer.validated_data['organizer'] = request.user
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
