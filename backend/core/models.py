from django.db import models
from accounts.models import Customer

class Card(models.Model):
    exercise_name = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    description = models.TextField()
    instructions = models.TextField()
    audio = models.FileField()
    duration = models.DurationField()

    def __str__(self):
        return self.exercise_name

class History(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    exercise_name = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.date_time