from django.db import models

from django.db import models

class WheelSpecification(models.Model):
    form_number = models.CharField(max_length=50, unique=True)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()
    status = models.CharField(max_length=50, default='Saved')

    fields = models.JSONField()

    def __str__(self):
        return self.form_number

