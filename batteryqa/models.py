from django.db import models
from django.utils.translation import ugettext_lazy as _


class Question(models.Model):
    MODEL = [('BatteryBERT-cased', 'BatteryBERT-cased'), ('BatterySciBERT-cased', 'BatterySciBERT-cased'),
             ('BatteryOnlyBERT-cased', 'BatteryOnlyBERT-cased'), ('BatteryBERT-uncased', 'BatteryBERT-uncased'),
             ('BatterySciBERT-uncased', 'BatterySciBERT-uncased'),
             ('BatteryOnlyBERT-uncased', 'BatteryOnlyBERT-uncased')]
    select = models.CharField(_('Select a model to analyse:'), choices=MODEL, max_length=25,
                              default='BatteryBERT-cased')
    confidence = models.FloatField(_('Confidence score threshold:'))
    ques = models.CharField(_('Ask a question:'), max_length=100)
    context = models.TextField(_(''))
    # answer = models.CharField(_('answer'), max_length=100, default='none')
    # score = models.FloatField(_('score'), default=0)

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')


class Search(models.Model):
    search = models.CharField(_(''), max_length=100)
