from django.db import models
from django.utils.translation import ugettext_lazy as _


class Question(models.Model):
    model_name = models.CharField(_('model_name'), max_length=64)
    confidence = models.FloatField(_('confidence'))
    ques = models.CharField(_('ques'), max_length=100)
    context = models.TextField(_('context'))
    answer = models.CharField(_('answer'), max_length=100, default='none')
    score = models.FloatField(_('score'), default=0)

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')
