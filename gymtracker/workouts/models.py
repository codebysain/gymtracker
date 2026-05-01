from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect


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
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return f"{self.exercise} - {self.reps} reps"

from .models import Exercise

def create_exercises(request):
    Exercise.objects.get_or_create(name="bench press")
    Exercise.objects.get_or_create(name="squat")
    Exercise.objects.get_or_create(name="deadlift")
    return redirect('workout_list')