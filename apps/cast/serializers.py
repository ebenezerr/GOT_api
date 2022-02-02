from rest_framework import serializers
from apps.cast.models import Character, Location, House


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("name", "lastname", "title", "house", "portrayed_by")

    def validate(self, attrs):
        name: str = attrs["name"]
        flag = False
        for c in name:
            if c.isnumeric():
                flag = True
                break
        if flag:
            raise serializers.ValidationError({
                "name": "invalid name."
            })
        return attrs


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "place"


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ("name", "location")