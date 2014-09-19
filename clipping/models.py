from __future__ import absolute_import

from django.contrib.gis.db import models
from django.conf import settings
from manipulators.models import BaseManipulatorGeometry

    
class Marine(BaseManipulatorGeometry):
    name = models.CharField(verbose_name="Marine Geometry Name", max_length=255,
                            blank=True)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, 
                                        null=True, blank=True, 
                                        verbose_name="Marine Only")

    def __unicode__(self):
        return "Marine Layer, created: %s" % (self.creation_date)

