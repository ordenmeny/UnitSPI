from rest_framework.serializers import ModelSerializer

from events_app.models.events import EventModel


class EventSerializer(ModelSerializer):
    class Meta:
        model = EventModel
        fields = '__all__'

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #
    #     data["hobby"] = HobbySerializer(instance.hobby.all(), many=True).data
    #     return data
