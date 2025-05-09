from django.db import models


class ClassificationEvent(models.Model):
    source = models.CharField(max_length=256)
    date_time = models.DateTimeField(auto_now=True)
    model_name = models.CharField(max_length=256, null=True, blank=True)
    classification = models.JSONField()
