from rest_framework import serializers
from .models import Character, Location, LogCharacter, Bounty, Hunter, ClaimBounty

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class BountySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bounty
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class LogCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogCharacter
        fields = '__all__'

class HunterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hunter
        fields = '__all__'

class ClaimBountySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimBounty
        fields = '__all__'
        