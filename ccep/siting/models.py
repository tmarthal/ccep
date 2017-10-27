from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.db import transaction

from datetime import date
class County(models.Model):

    name = models.TextField(_('County Name'), blank=False)
    geoid = models.TextField(_('County Name'), blank=False)

    active = models.BooleanField(_('Active'), default=False)

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    test = models.TextField(default='test')
    # Returns the string representation of the model.
    def __str__(self):
        return self.name

    class Meta:
        app_label = 'siting'
        db_table = 'counties'



class SitingModel(models.Model):
    name = models.TextField(_('Siting Model Name'), blank=False)
    description = models.TextField(_('Model Description'), default='siting model description')

    active = models.BooleanField(_('Active'), default=False)
    default = models.BooleanField(_('Default Model'), default=False)

    model_date = models.DateField(default=date.today)

    # a model must have a county
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.default:
            # if this model is default, remove default from other models
            SitingModel.objects.filter(default=True).update(default=False)
        super(SitingModel, self).save(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.county.name, self.name)

class ModelLayer(models.Model):
    name = models.TextField(_('Layer Name'), blank=False)
    description = models.TextField(_('Layer Description'), default='siting model description')

    # a model must have a county
    sitingModel = models.ForeignKey(SitingModel, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)
