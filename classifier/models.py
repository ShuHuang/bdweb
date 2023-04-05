from django.db import models
from django.utils.translation import ugettext_lazy as _


class TextClassifier(models.Model):
    text = models.TextField(_(''), max_length=100)
