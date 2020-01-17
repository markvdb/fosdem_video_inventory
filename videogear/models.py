from django.db import models


class VideoGear(models.Model):
    STATE = (
      (1,  'expected from rental company'),
      (2, 'pre FOSDEM inventoried'),
      (3, 'pre FOSDEM functionality checked'),
      (4, 'in room'),
      (5, 'post FOSDEM inventory OK'),
      (6, 'post FOSDEM NOK (add note!)'),
   )
    GEARTYPE = (
      (1,  'headphone'),
      (2, 'hand mic'),
      (3, 'tripod'),
      (4, 'camera'),
      (5, 'tiepin mic'),
   )
    rental_tag = models.CharField(max_length=20, blank=True)
    '''gear_type = models.PositiveSmallIntegerField(
      choices=GEARTYPE,
      default=1,
    )'''
    fosdem_tag = models.SlugField(unique=True, blank=True)
    gear_type = models.PositiveSmallIntegerField(
            choices=GEARTYPE,
            default=1,
    )
    notes = models.TextField(max_length=200, blank=True)
    state = models.PositiveSmallIntegerField(
      choices=STATE,
      default=1,
    )


    def __str__(self):
        return str(self.rental_tag)

