from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout, Set
from .forms import WorkoutForm, SetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


@login_required
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user).order_by('-date')
    date = request.GET.get('date')

    if date:
        workouts = workouts.filter(date=date)

    return render(request, 'workouts/list.html', {'workouts': workouts})

@login_required
def workout_create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()

    return render(request, 'workouts/create.html', {'form': form})

@login_required
def workout_update(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)

    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm(instance=workout)

    return render(request, 'workouts/update.html', {'form': form})

@login_required
def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)

    if request.method == 'POST':
        workout.delete()
        return redirect('workout_list')

    return render(request, 'workouts/delete.html', {'workout': workout})



@login_required
def add_set(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)

    if request.method == 'POST':
        form = SetForm(request.POST)
        if form.is_valid():
            set_obj = form.save(commit=False)
            set_obj.workout = workout
            set_obj.save()
            return redirect('workout_list')
    else:
        form = SetForm()

    return render(request, 'workouts/add_set.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('workout_list')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

@login_required
def edit_set(request, pk):
    set_obj = get_object_or_404(Set, pk=pk, workout__user=request.user)

    if request.method == 'POST':
        form = SetForm(request.POST, instance=set_obj)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = SetForm(instance=set_obj)

    return render(request, 'workouts/edit_set.html', {'form': form})

@login_required
def delete_set(request, pk):
    set_obj = get_object_or_404(Set, pk=pk, workout__user=request.user)

    if request.method == 'POST':
        set_obj.delete()
        return redirect('workout_list')

    return render(request, 'workouts/delete_set.html', {'set': set_obj})