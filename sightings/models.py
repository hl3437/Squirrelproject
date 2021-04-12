from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Squirrel(models.Model):
    Latitude = models.FloatField(
        max_length=17
        )

    Longitude = models.FloatField(
        max_length=17
        )

    Unique_Squirrel_ID = models.CharField(
        max_length=100
        )

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
        (AM, 'AM'),
        (PM, 'PM'),
    ]

    Shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES,
        )

    Date = models.DateField(
        help_text=_('Date in the form of MMDDYYYY'),
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = [
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
    ]

    Age = models.CharField(
        max_length=8,
        choices=AGE_CHOICES,
        blank=True,
        )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    PRIMARY_FUR_COLOR_CHOICES = [
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
    ]

    Primary_Fur_Color = models.CharField(
        max_length=20,
        choices=PRIMARY_FUR_COLOR_CHOICES,
        blank=True,
        )

    ABOVE_GROUND = 'Above Ground'
    GROUND_PLANE = 'Ground Plane'

    LOCATION_CHOICES = [
        (ABOVE_GROUND, 'Above Ground'),
        (GROUND_PLANE, 'Ground Plane'),
        ]

    Location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
        blank=True,
        )

    Specific_Location = models.CharField(
        max_length=100,
        blank=True,
        )

    Running = models.BooleanField(
        default=False,
        )

    Chasingg = models.BooleanField(
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

    Other_Activitiesg = models.CharField(
        max_length=100,
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
