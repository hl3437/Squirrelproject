from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Sight(models.Model):
    objects = None
    Longitude = models.FloatField(
        max_length=17,
        help_text=_('Longitude of the sighting'),
        blank=False,
        )

    Latitude = models.FloatField(
        max_length=17,
        help_text=_('Latitude of the sighting'), 
        blank=False,
        )

    Unique_Squirrel_Id = models.CharField(
        max_length=25,
        help_text=_('The unique ID of the squirrel'),
        blank=False,
        )
    
    AM = 'AM'
    PM = 'PM'
    
    SESSION = [
        (AM, 'AM'),
        (PM, 'PM'),
    ]

    Shift = models.CharField(
        max_length=16,
        help_text=_('Whether the sighting is in the morning or late afternoon?'),
        choices=SESSION,
        blank=False,
        )

    Date = models.DateField(
        help_text=_('(Date in the form of yyyy-mm-dd)'),
        blank=False,
        )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = '?'
    
    AGE_CHOICE = [
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
        (None, ''),
        (UNKNOWN, '?'),
    ]

    Age = models.CharField(
        max_length=8,
        help_text=_('Age of the squirrel'),
        choices=AGE_CHOICE,
        blank=True
        )

    BLACK = 'Black'
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    
    COLOR_CHOICE = [
        (BLACK, 'Black'),
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (None, ''),
    ]

    Primary_Fur_Color = models.CharField(
        max_length=16,
        help_text=_('Primary Fur color'),
        choices=COLOR_CHOICE,
        blank=True
        )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    
    LOCATION_CHOICE = [
        (GROUND_PLANE, 'Ground Plane'),
        (ABOVE_GROUND, 'Above Ground'),
        (None, ''),
    ]

    Location = models.CharField(
        max_length=20,
        help_text=_('Location'),
        choices=LOCATION_CHOICE,
        blank=True
        )

    Specific_Location = models.CharField(
        max_length=128,
        help_text=_('Additional notes to the location'),
        blank=True,
        )

    Running = models.BooleanField(
        default=False,
        )

    Chasing = models.BooleanField(
        default=False,
        )

    Climbing = models.BooleanField(
        default=False,
        )

    Eating = models.BooleanField(
        default=False,
        )

    Foraging = models.BooleanField(
        default=False,
        )

    Other_Activities = models.CharField(
        max_length=100,
        blank=True,
        )

    Kuks = models.BooleanField(
        default=False,
        )

    Quaas = models.BooleanField(
        default=False,
        )

    Moans = models.BooleanField(
        default=False,
        )

    Tail_flags = models.BooleanField(
        default=False,
        )

    Tail_twitches = models.BooleanField(
        default=False,
        )

    Approaches = models.BooleanField(
        default=False,
        )

    Indifferent = models.BooleanField(
        default=False,
        )

    Runs_from = models.BooleanField(
        default=False,
        )
