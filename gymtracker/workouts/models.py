from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.date}"


class Set(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='sets')
    exercise = models.CharField(max_length=100)  # ВОТ ЭТО
    reps = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return f"{self.exercise} - {self.reps} reps"