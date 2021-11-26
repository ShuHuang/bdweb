from django.db import models


class BatteryProperty(models.Model):
    """Battery Property Database"""
    property = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    raw_value = models.CharField(max_length=100)
    raw_unit = models.CharField(max_length=100)
    doi = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    journal = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    correctness = models.CharField(max_length=100)
    random = models.FloatField()
    unit = models.CharField(max_length=100)
    value = models.FloatField(max_length=100)
    num_records = models.FloatField()

#type	material	score	context	doi	title	journal	date	extracted_material
class BatteryDevice(models.Model):
    """Battery Device Database"""
    type = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    score = models.FloatField()
    context = models.TextField()
    doi = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    journal = models.CharField(max_length=100)
    date = models.CharField(max_length=100)