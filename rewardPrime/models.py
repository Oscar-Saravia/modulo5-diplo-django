from django.db import models
from django.core.exceptions import ValidationError
from .constants import StatusCharacter, GenderCharacter, SearchStatus, Currency
from .validators import isAdviceValidated, isAmountValidated
from django.utils.html import format_html

class Character(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=50,
        choices=StatusCharacter.choices,
        default=StatusCharacter.ALIVE
    )
    species = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=20,
        choices=GenderCharacter.choices,
        default=GenderCharacter.UNKNOWN
    )
    origin = models.CharField(max_length=100)
    last_location = models.CharField(max_length=100)
    image = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        return format_html(f'<img src="{self.image}" width="250" height="250" />')
    image_tag.short_description = 'Target'

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.TextField(max_length=100)
    type_location = models.TextField(max_length=100)
    dimension = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class LogCharacter(models.Model):
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.character_id.name

class Bounty(models.Model):
    title = models.CharField(
        max_length=50,
        blank=True, 
        null=True, 
    )
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE, default=1)
    search_status = models.CharField(
        max_length=10,
        choices=SearchStatus.choices,
        default=SearchStatus.ALIVE
    )
    description = models.TextField(
        max_length=200, 
        blank=True, 
        null=True, 
        validators=[isAdviceValidated,]
    )
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=1000, validators=[isAmountValidated])
    currency_type = models.CharField(
        max_length=4,
        choices=Currency.choices,
        default=Currency.USD
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.character_id.name} - {self.search_status} - {self.amount} {self.currency_type}"

class Hunter(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    image = models.URLField(max_length=200, blank=True, null=True)
    skill = models.TextField(
        max_length=200, 
        default='Unknown',
        validators=[isAdviceValidated,]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        return format_html(f'<img src="{self.image}" width="250" height="250" />')
    image_tag.short_description = 'Target'

    def __str__(self):
        return self.name
    
class ClaimBounty(models.Model):
    hunter_id = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    bounty_id = models.ForeignKey(Bounty, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    claimed = models.BooleanField(default=False)
    claimed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.hunter_id.name} - {self.bounty_id.character_id.name} - {self.bounty_id.search_status}"
    