from django.db import models
from django.utils.translation import ugettext_lazy as _

import uuid


class Question(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    MODEL = [('BatteryBERT', 'BatteryBERT'), ('BatterySciBERT', 'BatterySciBERT'),
             ('BatteryOnlyBERT', 'BatteryOnlyBERT')]
    select = models.CharField(_('Select a model to analyse:'), choices=MODEL, max_length=20, default='BatteryBERT')
    confidence = models.FloatField(_('Confidence score threshold:'))
    ques = models.CharField(_('Ask a question:'), max_length=100)
    context = models.TextField(_(''))
    # answer = models.CharField(_('answer'), max_length=100, default='none')
    # score = models.FloatField(_('score'), default=0)

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')