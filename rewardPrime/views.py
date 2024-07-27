from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view

from .models import Character, Bounty, Location, LogCharacter, Hunter, ClaimBounty
from .serializers import CharacterSerializer, BountySerializer, LocationSerializer, LogCharacterSerializer, HunterSerializer, ClaimBountySerializer

# Models View Sets
class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class BountyViewSet(viewsets.ModelViewSet):
    queryset = Bounty.objects.all()
    serializer_class = BountySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LogCharacterViewSet(viewsets.ModelViewSet):
    queryset = LogCharacter.objects.all()
    serializer_class = LogCharacterSerializer

class HunterViewSet(viewsets.ModelViewSet):
    queryset = Hunter.objects.all()
    serializer_class = HunterSerializer

class ClaimBountyViewSet(viewsets.ModelViewSet):
    queryset = ClaimBounty.objects.all()
    serializer_class = ClaimBountySerializer


# Generic Api View
class BountyApiView(generics.ListAPIView):
    queryset = Bounty.objects.all()
    serializer_class = BountySerializer

class LocationApiView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LogCharacterApiView(generics.ListAPIView):
    queryset = LogCharacter.objects.all()
    serializer_class = LogCharacterSerializer

class HunterApiView(generics.ListAPIView):
    queryset = Hunter.objects.all()
    serializer_class = HunterSerializer

# Custom API methods
@api_view(["GET"])
def getBannerCharacter(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    bounty = Bounty.objects.filter(character_id=character_id).first()
    
    if not bounty:
        return render(request, '404.html', status=status.HTTP_404_NOT_FOUND)

    return render(
        request,
        'bannerCharacter.html',
        {
            'character': character,
            'bounty': bounty,
        }
    )