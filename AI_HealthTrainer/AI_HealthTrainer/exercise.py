from django.shortcuts import render
from AI_HealthTrainer.models import Exercise
from AI_HealthTrainer.forms import ExerciseForm
from django.shortcuts import render, get_object_or_404, redirect
import json
from django.http import JsonResponse
from .models import Exercise


def exercise(request):
    exercises = Exercise.objects.all()
    
    # exercises_json = []
    # for exercise in exercises:
    #     exercise_data = {
    #         'id': exercise.id,
    #         'name': exercise.name,
    #     }
    #     exercises_json.append(exercise_data)
    # return JsonResponse({'exercises': exercises_json})
    

def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    # return render(request, 'exercise_detail.html', {'exercise': exercise})

def exercise_create(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm()
    # return render(request, 'exercise_form.html', {'form': form})

def exercise_update(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm(instance=exercise)
    # return render(request, 'exercise_form.html', {'form': form})

def exercise_delete(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect('exercise_list')
    # return render(request, 'exercise_confirm_delete.html', {'exercise': exercise})
    
    