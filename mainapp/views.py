from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Food, TimeWindow 

from django.forms import ModelForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

import datetime


class AddFoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name']


@login_required
def add_food(request):
    if request.POST:
        form = AddFoodForm(request.POST)
        if form.is_valid(): 		# ok to save to DB
            new_food = form.save()
            messages.success(request, str(new_food) + " was added!")

    return redirect('index')
    
       
@login_required
def delete_food(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    food.delete()
    messages.success(request, str(food) + " was deleted")

    return redirect('index')
 
@login_required
def eat_food(request, food_id, period_id):
    period = get_object_or_404(TimeWindow, pk=period_id)
    food = get_object_or_404(Food, pk=food_id)

    food.consumed_in_period.add(period)
    food.save()
    messages.success(request, str(food) + " was eaten!")

    return redirect('period', period_id=period_id)

@login_required
def uneat_food(request, food_id, period_id):
    period = get_object_or_404(TimeWindow, pk=period_id)
    food = get_object_or_404(Food, pk=food_id)

    food.consumed_in_period.remove(period)
    food.save()
    messages.success(request, str(food) + " was uneaten!")

    return redirect('period', period_id=period_id)

@login_required
def index(request, period_id=None):
    foods = Food.objects.all()
    add_form = AddFoodForm()

    start_date = datetime.date.today()
    end_date = start_date - datetime.timedelta(7)

    if period_id != None:
        time_window = get_object_or_404(TimeWindow, pk=period_id)
    else:
        time_window = TimeWindow.objects.filter(start_date__range=[end_date, start_date])[0]


    next_period = None
    previous_period = None

    try:
        next_period = time_window.get_next_by_start_date()
    except TimeWindow.DoesNotExist:
        next_date = time_window.start_date + datetime.timedelta(7)
        next_period = TimeWindow.objects.create(start_date=next_date)
        messages.success(request, "Added new time period")

    try:
        previous_period = time_window.get_previous_by_start_date()
    except TimeWindow.DoesNotExist:
        last_date = time_window.start_date - datetime.timedelta(7)
        previous_period = TimeWindow.objects.create(start_date=last_date)
        messages.success(request, "Added new time period")

    eaten_foods = foods.filter(consumed_in_period=time_window)
    uneaten_foods = foods.exclude(consumed_in_period=time_window)

    return render(request, "index.html", {'foods':foods, 'add_form':add_form, 'this_period':time_window, 'eaten_foods':eaten_foods, 'uneaten_foods':uneaten_foods, 'next_period':next_period, 'previous_period':previous_period})

