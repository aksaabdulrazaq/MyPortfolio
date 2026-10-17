from django.db import models

class Degree(models.Model):
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year_start = models.IntegerField()
    year_end = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.title} at {self.institution}"