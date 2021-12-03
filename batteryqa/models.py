from django.db import models
from django.utils.translation import ugettext_lazy as _


class Question(models.Model):
    model_name = models.CharField(_('select'), max_length=64)
    confidence = models.FloatField(_('input-score'))
    ques = models.CharField(_('input_question'), max_length=100)
    context = models.TextField(_('input_text'))
    # answer = models.CharField(_('answer'), max_length=100, default='none')
    # score = models.FloatField(_('score'), default=0)

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')