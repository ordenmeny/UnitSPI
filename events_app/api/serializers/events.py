from rest_framework.serializers import ModelSerializer

from events_app.api.serializers.users import UserSerializer
from events_app.models.events import EventModel


class EventSerializer(ModelSerializer):
    class Meta:
        model = EventModel
        fields = [
            'id',
            'title',
            'time',
            'location',
            'description',
            'tags',
            'joined_users',
            'organizer'
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["joined_users"] = UserSerializer(instance.joined_users.all(), many=True).data
        data["organizer"] = UserSerializer(instance.organizer).data
        return data


