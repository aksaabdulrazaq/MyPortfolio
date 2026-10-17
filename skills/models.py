from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50) # e.g. Python, HTML
    proficiency = models.IntegerField(help_text="Enter a number from 1-100") 

    def __str__(self):
        return self.name