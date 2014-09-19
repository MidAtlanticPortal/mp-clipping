from __future__ import absolute_import
from django.conf import settings
from clipping.models import Marine
from manipulators.manipulators import ClipToShapeManipulator, manipulatorsDict
import logging

very_small_area = .000000001

class ClipToShoreManipulator(ClipToShapeManipulator):
    def __init__(self, target_shape, **kwargs):
        self.zero = very_small_area
        self.target_shape = target_shape
        try:
            self.clip_against = Marine.objects.current().geometry
            self.clip_against.transform(settings.GEOMETRY_CLIENT_SRID)
        except Exception:
            logging.getLogger('clipping.manipulators').exception('Exception raised in ClipToShoreManipulator while obtaining marine-manipulator geometry from database.')
            raise    

    class Options:    
        name = 'ClipToShoreManipulator'
        display_name = 'Clip to Shoreline'
        description = 'Removes any part of your shape that is not Marine.'
        supported_geom_fields = ['PolygonField']

        html_templates = {
            '0': 'clipping/marine_only.html',
            '2': 'clipping/empty_result.html',
        }

manipulatorsDict[ClipToShoreManipulator.Options.name] = ClipToShoreManipulator
